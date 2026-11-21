class ClothingStore:
    def __init__(
        self,
        name: str,
        products: dict[str, float],
        regular_customers: dict[str, int],
        cumulative_step: float,
        seasonal_discount: float,
        time_discount: float,
    ) -> None:
        self.name = name
        self.products = products
        self.regular_customers = regular_customers
        self.cumulative_step = cumulative_step
        self.seasonal_discount = seasonal_discount
        self.time_discount = time_discount

    def calc_cumulative_discount(self, customer_name: str) -> float:
        orders_count = self.regular_customers.get(customer_name, 0)
        return min(30.0, orders_count * self.cumulative_step)

    def calc_seasonal_discount(self, month: int) -> float:
        if month in (1, 2, 7, 8):
            return self.seasonal_discount
        return self.seasonal_discount / 2

    def calc_time_discount(self, hour: int) -> float:
        if 10 <= hour <= 13:
            return self.time_discount
        return 0.0

    def calculate_final_price(
        self, product_name: str, customer_name: str, month: int, hour: int
    ) -> tuple[float, float, float, float]:
        base_price = self.products[product_name]
        d_cum = self.calc_cumulative_discount(customer_name)
        d_sea = self.calc_seasonal_discount(month)
        d_time = self.calc_time_discount(hour)
        total_discount = min(50.0, d_cum + d_sea + d_time)
        final_price = base_price * (1 - total_discount / 100)
        return base_price, total_discount, final_price, d_cum

    def __str__(self) -> str:
        return (
            f"Store: {self.name} | Products: {len(self.products)} | "
            f"Regular customers: {len(self.regular_customers)}"
        )


store_name = input("Enter store name: ").strip()

products_count = int(input("Enter number of products: "))
products: dict[str, float] = {}
for _ in range(products_count):
    p_name = input("  Product name: ").strip()
    p_price = float(input("  Product price: "))
    products[p_name] = p_price

customers_count = int(input("Enter number of regular customers: "))
regular_customers: dict[str, int] = {}
for _ in range(customers_count):
    c_name = input("  Customer name: ").strip()
    c_orders = int(input("  Number of past purchases: "))
    regular_customers[c_name] = c_orders

cum_step = float(input("Enter cumulative discount per purchase (%): "))
sea_disc = float(input("Enter seasonal discount (%): "))
time_disc = float(input("Enter off-peak time discount for 10:00-13:00 (%): "))

store = ClothingStore(
    store_name, products, regular_customers, cum_step, sea_disc, time_disc
)

print(f"\n{store}")
print("Catalog:")
for item, price in store.products.items():
    print(f"  - {item}: {price:.2f} UAH")

print("Regular customers and cumulative discounts:")
for cust in store.regular_customers:
    print(f"  - {cust}: {store.calc_cumulative_discount(cust):.1f}%")

selected_product = input("\nEnter product to buy: ").strip()
buyer_name = input("Enter buyer name: ").strip()
visit_month = int(input("Enter month (1..12): "))
visit_hour = int(input("Enter visit hour (0..23): "))

if selected_product in store.products:
    base, total_d, final, _ = store.calculate_final_price(
        selected_product, buyer_name, visit_month, visit_hour
    )
    print(
        "Calculation for {} | Buyer: {} | Base: {:.2f} UAH | Total discount: {:.1f}% | Final price: {:.2f} UAH".format(
            selected_product, buyer_name, base, total_d, final
        )
    )
else:
    print(f"Product '{selected_product}' not found in catalog.")