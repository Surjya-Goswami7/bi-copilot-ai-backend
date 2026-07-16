import pandas as pd


class DatasetAnalyzer:

    # ----------------------------
    # Detect Dataset Type
    # ----------------------------
    @staticmethod
    def detect_dataset_type(df: pd.DataFrame):

        columns = [str(col).lower() for col in df.columns]

        sales_keywords = [
            "sales", "revenue", "profit", "quantity",
            "customer", "product", "discount"
        ]

        hr_keywords = [
            "employee", "salary", "department",
            "joining", "designation"
        ]

        finance_keywords = [
            "account", "expense", "income",
            "balance", "transaction"
        ]

        inventory_keywords = [
            "stock", "warehouse", "inventory",
            "supplier"
        ]

        if any(keyword in " ".join(columns) for keyword in sales_keywords):
            return "Sales"

        elif any(keyword in " ".join(columns) for keyword in hr_keywords):
            return "HR"

        elif any(keyword in " ".join(columns) for keyword in finance_keywords):
            return "Finance"

        elif any(keyword in " ".join(columns) for keyword in inventory_keywords):
            return "Inventory"

        return "Unknown"

    # ----------------------------
    # Detect Measures
    # ----------------------------
    @staticmethod
    def detect_measures(df: pd.DataFrame):

        measures = []

        keywords = [
            "sales",
            "profit",
            "revenue",
            "amount",
            "quantity",
            "cost",
            "price",
            "margin",
            "discount"
        ]

        for col in df.columns:

            if any(word in str(col).lower() for word in keywords):
                measures.append(col)

        return measures

    # ----------------------------
    # Detect Dimensions
    # ----------------------------
    @staticmethod
    def detect_dimensions(df: pd.DataFrame):

        dimensions = []

        keywords = [
            "customer",
            "product",
            "category",
            "region",
            "country",
            "city",
            "state",
            "segment",
            "department"
        ]

        for col in df.columns:

            if any(word in str(col).lower() for word in keywords):
                dimensions.append(col)

        return dimensions

    # ----------------------------
    # Detect Date Columns
    # ----------------------------
    @staticmethod
    def detect_date_columns(df: pd.DataFrame):

        date_columns = []

        keywords = [
            "date",
            "month",
            "year",
            "day",
            "time"
        ]

        for col in df.columns:

            if any(word in str(col).lower() for word in keywords):
                date_columns.append(col)

        return date_columns

    # ----------------------------
    # Detect Primary Keys
    # ----------------------------
    @staticmethod
    def detect_primary_keys(df: pd.DataFrame):

        primary_keys = []

        keywords = [
            "id",
            "code",
            "number",
            "key"
        ]

        for col in df.columns:

            if any(word in str(col).lower() for word in keywords):

                if df[col].is_unique:
                    primary_keys.append(col)

        return primary_keys

    # ----------------------------
    # Complete Analysis
    # ----------------------------
    @staticmethod
    def analyze(df: pd.DataFrame):

        return {

            "dataset_type":
                DatasetAnalyzer.detect_dataset_type(df),

            "measures":
                DatasetAnalyzer.detect_measures(df),

            "dimensions":
                DatasetAnalyzer.detect_dimensions(df),

            "date_columns":
                DatasetAnalyzer.detect_date_columns(df),

            "possible_primary_keys":
                DatasetAnalyzer.detect_primary_keys(df)
        }