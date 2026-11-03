STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a list of (stock, qty, value)."""
    holdings = []
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nEnter a stock name and quantity. Type 'done' as the stock name to finish.\n")

    while True:
        name = input("Stock name: ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Unknown stock. Please choose from the list above.\n")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a whole number greater than 0.\n")
            continue

        qty = int(qty_text)
        value = STOCK_PRICES[name] * qty
        holdings.append((name, qty, value))
        print(f"Added {qty} x {name} = ${value}\n")

    return holdings


def show_summary(holdings):
    total = sum(value for _, _, value in holdings)
    print("\n=== PORTFOLIO SUMMARY ===")
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>12}")
    for name, qty, value in holdings:
        print(f"{name:<8}{qty:>6}{STOCK_PRICES[name]:>10}{value:>12}")
    print("-" * 36)
    print(f"{'Total investment:':<24}${total}")
    return total


def save_to_file(holdings, total, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write("PORTFOLIO SUMMARY\n")
        for name, qty, value in holdings:
            f.write(f"{name}: {qty} x ${STOCK_PRICES[name]} = ${value}\n")
        f.write(f"Total investment: ${total}\n")
    print(f"Saved to {filename}")


def main():
    holdings = get_portfolio()
    if not holdings:
        print("No stocks entered.")
        return

    total = show_summary(holdings)

    save = input("\nSave result to portfolio.txt? (y/n): ").strip().lower()
    if save == "y":
        save_to_file(holdings, total)


if __name__ == "__main__":
    main()