import json
from typing import Any
from jsontoinput import converter
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="n8n2py Converted Workflow")


def run_workflow(input_data: dict | list | None = None) -> dict[str, Any]:
    """
    Simulazione del workflow n8n: "Extract-Info to prompt" (6 nodi).
    Per ora i nodi sono placeholder generici, pronti per essere collegati
    alla logica reale (LangChain, LLM, ecc.).
    """
    workflow_result: dict[str, Any] = {
        "input": input_data,
        "nodes": {},
        "success": True,
    }

    try:
        # Nodo 1: when_chat_message_received
        when_chat_message_received_result = {
            "success": True,
            "data": "Generic LangChain node executed",
            "node_type": "@n8n/n8n-nodes-langchain.chatTrigger",
            "parameters": {
                "options": {}
            },
            "note": (
                "This is a generic implementation. Consider adding specific "
                "handling for this node type."
            ),
        }
        print(
            "Generic LangChain node executed: "
            "@n8n/n8n-nodes-langchain.chatTrigger"
        )
        workflow_result["nodes"]["when_chat_message_received"] = (
            when_chat_message_received_result
        )

        # Nodo 2: ai_agent
        ai_agent_result = {
            "success": True,
            "data": "Generic LangChain node executed",
            "node_type": "@n8n/n8n-nodes-langchain.agent",
            "parameters": {
                "hasOutputParser": True,
                "options": {},
            },
            "note": (
                "This is a generic implementation. Consider adding specific "
                "handling for this node type."
            ),
        }
        print(
            "Generic LangChain node executed: "
            "@n8n/n8n-nodes-langchain.agent"
        )
        workflow_result["nodes"]["ai_agent"] = ai_agent_result

        # Nodo 3: simple_memory
        simple_memory_result = {
            "success": True,
            "data": "Generic LangChain node executed",
            "node_type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
            "parameters": {},
            "note": (
                "This is a generic implementation. Consider adding specific "
                "handling for this node type."
            ),
        }
        print(
            "Generic LangChain node executed: "
            "@n8n/n8n-nodes-langchain.memoryBufferWindow"
        )
        workflow_result["nodes"]["simple_memory"] = simple_memory_result

        # Nodo 4: structured_output_parser
        diagnosis_schema = (
            '{\n'
            '  "$schema": "http://json-schema.org/draft-07/schema#",\n'
            '  "title": "DiagnosisProbability",\n'
            '  "type": "object",\n'
            '  "properties": {\n'
            '    "conditions": {\n'
            '      "type": "array",\n'
            '      "minItems": 1,\n'
            '      "items": {\n'
            '        "type": "object",\n'
            '        "properties": {\n'
            '          "name": { "type": "string", "description": "Nome della condizione/malattia" },\n'
            '          "icd10": { "type": "string", "description": "Codice ICD-10 se noto" },\n'
            '          "probability_percent": { "type": "number", "minimum": 0, "maximum": 100 },\n'
            '          "rationale": { "type": "string", "description": "Breve motivazione clinica" }\n'
            '        },\n'
            '        "required": ["name", "probability_percent"]\n'
            '      }\n'
            '    },\n'
            '    "notes": {\n'
            '      "type": "string",\n'
            '      "description": "Assunzioni o limiti della valutazione",\n'
            '      "default": ""\n'
            '    }\n'
            '  },\n'
            '  "required": ["conditions"]\n'
            '}\n'
        )

        structured_output_parser_result = {
            "success": True,
            "data": "Generic LangChain node executed",
            "node_type": "@n8n/n8n-nodes-langchain.outputParserStructured",
            "parameters": {
                "schemaType": "manual",
                "inputSchema": diagnosis_schema,
                "autoFix": True,
            },
            "note": (
                "This is a generic implementation. Consider adding specific "
                "handling for this node type."
            ),
        }
        print(
            "Generic LangChain node executed: "
            "@n8n/n8n-nodes-langchain.outputParserStructured"
        )
        workflow_result["nodes"]["structured_output_parser"] = (
            structured_output_parser_result
        )

        # Nodo 5: google_gemini_chat_model
        google_gemini_chat_model_result = {
            "success": True,
            "data": "Generic LangChain node executed",
            "node_type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
            "parameters": {
                "options": {}
            },
            "note": (
                "This is a generic implementation. Consider adding specific "
                "handling for this node type."
            ),
        }
        print(
            "Generic LangChain node executed: "
            "@n8n/n8n-nodes-langchain.lmChatGoogleGemini"
        )
        workflow_result["nodes"]["google_gemini_chat_model"] = (
            google_gemini_chat_model_result
        )

        # Nodo 6: google_gemini_chat_model1 (seconda istanza)
        google_gemini_chat_model1_result = {
            "success": True,
            "data": "Generic LangChain node executed",
            "node_type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
            "parameters": {
                "options": {}
            },
            "note": (
                "This is a generic implementation. Consider adding specific "
                "handling for this node type."
            ),
        }
        print(
            "Generic LangChain node executed: "
            "@n8n/n8n-nodes-langchain.lmChatGoogleGemini (second instance)"
        )
        workflow_result["nodes"]["google_gemini_chat_model1"] = (
            google_gemini_chat_model1_result
        )

    except Exception as exc:
        print(f"Error while running workflow: {exc}")
        workflow_result["success"] = False
        workflow_result["error"] = str(exc)

    return workflow_result


@app.get("/")
async def root():
    return {"ok": True}


@app.post("/run")
async def run(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = None

    result = run_workflow(data)
    return JSONResponse(result)


if __name__ == "__main__":
    # Esecuzione locale semplice, utile per il debug
    print("Running workflow...")
    result = run_workflow(converter())
    print("Done. Result:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
