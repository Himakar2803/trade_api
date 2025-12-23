def fetch_market_data(sector):
    # Dummy static dataset (replace with API real data later)
    example_data = {
        "technology": {
            "companies": ["Apple", "Microsoft", "Google"],
            "trend": "bullish",
            "growth": "strong"
        },
        "finance": {
            "companies": ["JPMorgan", "Goldman Sachs"],
            "trend": "stable",
            "growth": "moderate"
        }
    }

    return example_data.get(sector, {"message": "No market data found"})
