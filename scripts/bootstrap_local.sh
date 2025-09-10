
#!/bin/bash

# Backend
cd backend
# Python 3.12 required - 3.13 has wheel compilation issues
python3.12 -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt
cd ..

# Frontend  
cd frontend
pnpm install
cd ..

echo "Setup complete!"
echo "To run backend: cd backend && source .venv/bin/activate && uvicorn app.main:app --reload"
echo "To run frontend: cd frontend && pnpm dev"