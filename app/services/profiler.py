import pandas as pd


class DatasetProfiler:

    @staticmethod
    def profile(df: pd.DataFrame):

        profile = {

            "row_count": len(df),

            "column_count": len(df.columns),

            "column_names": df.columns.tolist(),

            "missing_values": df.isnull().sum().to_dict(),

            "duplicate_rows": int(df.duplicated().sum()),

            "numeric_columns": df.select_dtypes(
                include=["number"]
            ).columns.tolist(),

            "categorical_columns": df.select_dtypes(
                include=["object", "category"]
            ).columns.tolist(),

            "date_columns": df.select_dtypes(
                include=["datetime64"]
            ).columns.tolist(),

            "memory_usage_mb": round(
                df.memory_usage(deep=True).sum() / (1024 * 1024),
                2
            )

        }

        return profile