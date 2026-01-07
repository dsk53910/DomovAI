from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_ollama import ChatOllama

app = FastAPI(title="Domovai AI Service", version="1.0.0")

class CodeReviewRequest(BaseModel):
    code: str
    language: str = "python"

class CodeReviewResponse(BaseModel):
    review: str
    bugs_found: bool

model_name = "qwen2.5-coder:7b"
llm = ChatOllama(model=model_name, temperature=0.2)

@app.post("/review", response_model=CodeReviewResponse)
async def review_code(request: CodeReviewRequest):
    prompt = f" Your are senior code reviewer. Review the following {request.language} code for bugs and improvements:\n\n{request.code}"
    
    try:
        response = llm.invoke(prompt)
        
        review_text = response.content
        bugs_found = "bug" in review_text.lower() or "error" in review_text.lower() or "issue" in review_text.lower()
        
        return CodeReviewResponse(review=review_text, bugs_found=bugs_found)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/health")
def health():
    return {"status": "ok", "model": model_name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)