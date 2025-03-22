from pydantic import BaseModel

class FinancialData(BaseModel):
    """Base model for financial data"""
    pass

def main():
    """Main entry point for the application"""
    print("Finance Advisor - A system to help with financial decisions")

if __name__ == "__main__":
    main() 