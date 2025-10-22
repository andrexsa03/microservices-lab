import os
import psycopg2
import redis

# Cargar variables de entorno
POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

print("🔍 Probando conexión con PostgreSQL...")
try:
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    print("✅ Conexión a PostgreSQL exitosa.")
    conn.close()
except Exception as e:
    print("❌ Error al conectar a PostgreSQL:", e)

print("\n🔍 Probando conexión con Redis...")
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    r.ping()
    print("✅ Conexión a Redis exitosa.")
except Exception as e:
    print("❌ Error al conectar a Redis:", e)
