#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from typing import Any, Callable, Dict, Generator, List

from sgpt.config import cfg

completion: Callable[..., Any] = lambda *args, **kwargs: Generator[Any, None, None]

azure_openai_api_key = cfg.get("AZURE_OPENAI_API_KEY")
azure_openai_api_version = cfg.get("AZURE_OPENAI_API_VERSION")
azure_openai_api_endpoint = cfg.get("AZURE_OPENAI_API_ENDPOINT")

from openai import AzureOpenAI

print(f"Using Azure OpenAI v{azure_openai_api_version}")
client = AzureOpenAI(
    api_key=azure_openai_api_key,
    api_version=azure_openai_api_version,
    azure_endpoint=azure_openai_api_endpoint
)


def make_messages(prompt: str) -> List[Dict[str, str]]:
    messages = [{"role": "user", "content": prompt}]
    return messages


response = client.chat.completions.create(
    model=cfg.get("DEFAULT_MODEL"),
    temperature=0.2,
    top_p=1,
    messages=make_messages('hello'),
    stream=True,
)
for chunk in response:
    print(f"{chunk=}")
