"""
mining_ecommerce.py

Custom BI project: E-Commerce Growth Analytics

Author: Your Name
Date: 2026-07

Run:
uv run python -m bizintel.mining_ecommerce
"""

from pathlib import Path
from typing import Final

import pandas as pd
import matplotlib.pyplot as plt

from datafun_toolkit.logger import log_path
from bizintel.utils_data import (
    load_data,
    inspect_basic,
    check_quality,
    summarize_numeric,
)
from bizintel.utils_logger import LOG, log_header
from bizintel.utils_viz import plot_line


# =========================
# FILE PATHS
# =========================

DATA_RAW: Final[Path] = Path("data/raw")

CUSTOMERS_FILE: Final[Path] = DATA_RAW / "customers.csv"
ORDERS_FILE: Final[Path] = DATA_RAW / "orders.csv"
WEB_FILE: Final[Path] = DATA_RAW / "web_activity.csv"


# =========================
# ANALYSIS FUNCTIONS
# =========================

def plot_order_distribution(df_orders: pd.DataFrame) -> None:
    LOG.info("Plotting order amount distribution")

    amounts = pd.to_numeric(df_orders["OrderAmount"], errors="coerce")

    _, ax = plt.subplots(figsize=(9, 5))
    ax.hist(amounts.dropna(), bins=10, color="seagreen", edgecolor="white")

    ax.set_title("Order Amount Distribution")
    ax.set_xlabel("Order Amount ($)")
    ax.set_ylabel("Number of Orders")

    plt.tight_layout()


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

    LOG.info("Insight: Engagement data can be linked to revenue behavior.")


# =========================
# MAIN
# =========================

def main() -> None:
    log_header(LOG, "E-COMMERCE BI")

    LOG.info("Starting workflow...")

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
