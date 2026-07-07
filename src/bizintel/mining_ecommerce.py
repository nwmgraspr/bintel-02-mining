"""
mining_ecommerce.py

Custom BI project: E-Commerce Growth Analytics

Run:
uv run python -m bizintel.mining_ecommerce
"""

from pathlib import Path
from typing import Final

from datafun_toolkit.logger import log_path
import matplotlib.pyplot as plt
import pandas as pd

from bizintel.utils_data import (
    check_quality,
    inspect_basic,
    load_data,
    summarize_numeric,
)
from bizintel.utils_logger import LOG, log_header
from bizintel.utils_viz import plot_line

# =========================
# AUTO DATA GENERATION
# =========================


def create_sample_data(data_dir: Path) -> None:
    """Create sample CSV files if missing (self-contained project)."""

    data_dir.mkdir(parents=True, exist_ok=True)

    customers_file = data_dir / "customers.csv"
    orders_file = data_dir / "orders.csv"
    web_file = data_dir / "web_activity.csv"

    # If already exists → do nothing
    if customers_file.exists() and orders_file.exists() and web_file.exists():
        return

    customers = """CustomerID,Name,Country,SignupDate,LoyaltyTier
C001,Alice Johnson,USA,2025-01-10,Gold
C002,Brian Smith,USA,2025-02-15,Silver
C003,Chen Wei,Canada,2025-03-20,Bronze
C004,Diana Lopez,Mexico,2025-04-05,Silver
C005,Emma Brown,USA,2025-05-18,Gold
C006,Faisal Khan,UK,2025-06-01,Bronze
C007,Grace Kim,South Korea,2025-06-10,Silver
C008,Hassan Ali,USA,2025-06-25,Bronze
"""

    orders = """OrderID,CustomerID,OrderDate,OrderAmount,ProductCategory
O1001,C001,2026-01-05,120.50,Electronics
O1002,C002,2026-01-10,35.99,Books
O1003,C003,2026-01-12,89.99,Home
O1004,C001,2026-02-01,220.00,Electronics
O1005,C004,2026-02-15,45.00,Fashion
O1006,C005,2026-03-01,310.25,Electronics
O1007,C006,2026-03-05,25.00,Books
O1008,C007,2026-03-10,150.75,Home
O1009,C008,2026-03-15,99.99,Fashion
O1010,C002,2026-04-01,60.00,Books
"""

    web = """SessionID,CustomerID,VisitDate,PagesViewed,TimeSpentMinutes
S001,C001,2026-01-05,12,18
S002,C002,2026-01-10,5,7
S003,C003,2026-01-12,8,12
S004,C001,2026-02-01,20,30
S005,C004,2026-02-15,6,10
S006,C005,2026-03-01,25,40
S007,C006,2026-03-05,4,5
S008,C007,2026-03-10,15,22
S009,C008,2026-03-15,10,14
S010,C002,2026-04-01,7,9
"""

    customers_file.write_text(customers)
    orders_file.write_text(orders)
    web_file.write_text(web)

    print("✅ Sample data created in data/raw/")


# =========================
# CONFIG PATHS
# =========================

DATA_RAW: Final[Path] = Path("data/raw")

CUSTOMERS_FILE: Final[Path] = DATA_RAW / "customers.csv"
ORDERS_FILE: Final[Path] = DATA_RAW / "orders.csv"
WEB_FILE: Final[Path] = DATA_RAW / "web_activity.csv"


# =========================
# ANALYSIS FUNCTIONS
# =========================


def plot_order_distribution(df_orders: pd.DataFrame) -> None:
    LOG.info("Plotting order distribution")

    amounts = pd.to_numeric(df_orders["OrderAmount"], errors="coerce")

    _, ax = plt.subplots(figsize=(9, 5))
    ax.hist(amounts.dropna(), bins=10, color="seagreen", edgecolor="white")

    ax.set_title("Order Amount Distribution")
    ax.set_xlabel("Order Amount ($)")
    ax.set_ylabel("Number of Orders")


def plot_revenue_trend(df_orders: pd.DataFrame) -> None:
    LOG.info("Plotting revenue trend")

    df = df_orders.copy()

    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    df["OrderAmount"] = pd.to_numeric(df["OrderAmount"], errors="coerce")

    df["YearMonth"] = df["OrderDate"].dt.to_period("M")

    grouped = df.groupby("YearMonth")["OrderAmount"].sum().reset_index()
    grouped["YearMonth"] = grouped["YearMonth"].astype(str)

    plot_line(
        df=grouped,
        x="YearMonth",
        y="OrderAmount",
        title="Monthly Revenue Trend",
        xlabel="Month",
        ylabel="Revenue ($)",
    )


def plot_engagement_vs_spending(df_orders, df_web) -> None:
    LOG.info("Plotting engagement vs spending")

    orders = df_orders.groupby("CustomerID")["OrderAmount"].sum().reset_index()
    web = df_web.groupby("CustomerID")["TimeSpentMinutes"].sum().reset_index()

    merged = pd.merge(orders, web, on="CustomerID", how="inner")

    _, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(merged["TimeSpentMinutes"], merged["OrderAmount"], color="purple")

    ax.set_title("Engagement vs Spending")
    ax.set_xlabel("Time Spent (Minutes)")
    ax.set_ylabel("Total Spend ($)")


def summarize(df_customers, df_orders, df_web) -> None:
    LOG.info("========================")
    LOG.info("SUMMARY")
    LOG.info("========================")

    LOG.info(f"Customers: {df_customers.shape}")
    LOG.info(f"Orders:    {df_orders.shape}")
    LOG.info(f"Web:       {df_web.shape}")


# =========================
# MAIN PIPELINE
# =========================


def main() -> None:
    log_header(LOG, "E-COMMERCE BI")

    LOG.info("Starting workflow...")

    # 👇 AUTO-CREATE DATA IF MISSING
    create_sample_data(DATA_RAW)

    log_path(LOG, "Customers:", CUSTOMERS_FILE)
    log_path(LOG, "Orders:", ORDERS_FILE)
    log_path(LOG, "Web:", WEB_FILE)

    df_customers = load_data(CUSTOMERS_FILE, "customers")
    df_orders = load_data(ORDERS_FILE, "orders")
    df_web = load_data(WEB_FILE, "web")

    inspect_basic(df_customers, "customers")
    inspect_basic(df_orders, "orders")
    inspect_basic(df_web, "web")

    check_quality(df_customers, "customers")
    check_quality(df_orders, "orders")
    check_quality(df_web, "web")

    summarize_numeric(df_orders, "orders")

    plot_order_distribution(df_orders)
    plot_revenue_trend(df_orders)
    plot_engagement_vs_spending(df_orders, df_web)

    summarize(df_customers, df_orders, df_web)

    plt.show()

    LOG.info("Done.")


if __name__ == "__main__":
    main()
