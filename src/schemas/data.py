from pydantic import BaseModel, Field, model_validator

# ==========================================
# MAIN SCHEMA (REQUEST)
# ==========================================

class ModelDataValidator(BaseModel):
    pass

# ==========================================
# RESPONSE SCHEMA (WHAT IS RETURNED)
# ==========================================

class ModelDataResponse(BaseModel):
    pass