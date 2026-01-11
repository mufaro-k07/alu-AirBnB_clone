#!/usr/bin/python3
"""Test BaseModel: save() method"""
from models.base_model import BaseModel
import time

model = BaseModel()
old_updated_at = model.updated_at

time.sleep(0.01)
model.save()

if model.updated_at > old_updated_at:
    print("OK")
else:
    print("Error: save() did not update updated_at")