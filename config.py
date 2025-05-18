STANDARD_COLUMNS = ["Date", "Description", "Amount", "Category", "Institution"]

DATA_PATHS = [
    "sample_data/institution_1.csv",
    "sample_data/institution_2.csv",
]

IGNORED_CATEGORIES = ["Internal Transfer", "Credit Card Payment", "Refund"]

# Rules for categorizing transactions based on description keywords
CATEGORIZATION_RULES = {
    "Grocery": ["grocery", "supermarket", "food mart"],
    "Dining": ["restaurant", "dining", "cafe", "bistro"],
    "Gas": ["gas", "fuel", "petrol"],
    "Shopping": ["retail", "store", "mall", "online"],
    "Utilities": ["electric", "water", "utility", "internet"],
}
