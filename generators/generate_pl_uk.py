import asyncio
import aiohttp
import os
from .common import CATEGORIES_B1, WORDS_PER_CHUNK, api_request, save_csv_chunks
from .validator import ValidationService

async def process(session: aiohttp.ClientSession, semaphore: asyncio.Semaphore, base_dir: str):
    lang_source = "pl"
    lang_target = "uk"
    validator = ValidationService(lang_source, lang_target)
    pair_dir = os.path.join(base_dir, f"{lang_source}-{lang_target}")
    if not os.path.exists(pair_dir):
        os.makedirs(pair_dir)
        
    for category, subcategories in CATEGORIES_B1.items():
        file_path = os.path.join(pair_dir, f"{lang_source}-{lang_target}_{category}.csv")
        
        if os.path.exists(file_path):
            print(f"Skipping {file_path}, already exists.")
            continue
            
        with open("generators/prompt_templates/polish_ukrainian_prompt.md", "r", encoding="utf-8") as f:
            template = f.read()

        tasks = []
        for subcategory in subcategories:
            prompt = template.format(WORDS_PER_CHUNK=WORDS_PER_CHUNK, category=category, subcategory=subcategory)
            task = asyncio.create_task(api_request(session, semaphore, prompt, category, subcategory))
            tasks.append(task)
            
        results = await asyncio.gather(*tasks)
        await save_csv_chunks(results, file_path, validator)
