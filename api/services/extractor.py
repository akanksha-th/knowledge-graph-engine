from api.core.config import get_settings
from api.schema.graph import KnowledgeGraph
from groq import AsyncGroq
import json

settings = get_settings()
PROMPT_TEMPLATE = """
You will be given a piece of text. You must analyze the text thoroughly and generate triples from it (subject, predicate and object). Do NOT skip any possible, true triple.

For example: 
TEXT: "I ate one fried egg with a runny yolk. The toast was too dark and crisp. My coffee had cream and sugar in it."

The generated output will be in the provided JSON format:
{{
  "triples": [
    {{
      "subject": "I",
      "predicate": "ate",
      "object": "one fried egg"
    }},
    {{
      "subject": "fried egg",
      "predicate": "has",
      "object": "runny yolk"
    }},
    {{
      "subject": "toast",
      "predicate": "is",
      "object": "too dark"
    }},
    {{
      "subject": "toast",
      "predicate": "is",
      "object": "crisp"
    }},
    {{
      "subject": "coffee",
      "predicate": "contains",
      "object": "cream"
    }},
    {{
      "subject": "coffee",
      "predicate": "contains",
      "object": "sugar"
    }}
  ]
}}
Now, analyze the following text and generate triples in the same format:
TEXT: "{text}"

Do NOT give any explanations, only answer in the specified format.
Do NOT force any triple. ONLY extract complete triples.
"""

class TripleExtractionService:
    def __init__(self):
        self.client = AsyncGroq(api_key=settings.groq_api_key)

    async def build_kg(self, text: str) -> KnowledgeGraph:
        try:
            raw_response = await self.client.chat.completions.create(
                model=settings.model_name,
                messages=[{
                    "role": "system", 
                    "content": PROMPT_TEMPLATE.format(text=text), 
                    "max_tokens": 10000,
                }]
            )
            return self._parse_json(raw_response.choices[0].message.content)
        except Exception as e:
            raise ValueError(f"Failed to extract triples: {e}")

    def _parse_json(self, text: str) -> KnowledgeGraph:
        text = text.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            text = "\n".join(lines[1:-1]).strip()
        try:
            data = json.loads(text)
            if not data or "triples" not in data:
                raise ValueError("No triples found in the response")
            return KnowledgeGraph(**data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON: {e}")
