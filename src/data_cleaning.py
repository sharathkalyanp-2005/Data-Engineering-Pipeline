from pyspark.sql.functions import col, when, to_date, avg

def clean_customers(customers_df):
    customers_df = customers_df.withColumn(
        "name", when((col("name")=="##INVALID##")|(col("name").isNull()), None).otherwise(col("name"))
    )
    customers_df = customers_df.withColumn(
        "email", when((col("email")=="None")|(col("email").isNull()), None).otherwise(col("email"))
    )
    customers_df = customers_df.withColumnRenamed("name","customer_name")
    return customers_df

def clean_orders(orders_df):
    orders_df = orders_df.withColumn("order_date", to_date("order_date", "yyyy-MM-dd"))
    orders_df = orders_df.withColumn("amount", when(col("amount") <= 0, 0).otherwise(col("amount")))
    return orders_df

def clean_products(products_df):
    category_avg = products_df.groupBy("category").agg(avg("price").alias("avg_price"))
    products_df = products_df.join(category_avg, on="category", how="left")
    products_df = products_df.withColumn("price", when(col("price") <= 0, col("avg_price")).otherwise(col("price")))
    products_df = products_df.drop("avg_price")
    products_df = products_df.withColumnRenamed("name", "product_name")
    return products_df
