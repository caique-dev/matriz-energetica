import duckdb

# Cria ou abre o banco
con = duckdb.connect("nome do banco")

# Cria tabelas
con.execute("""
CREATE TABLE IF NOT EXISTS paises (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    continente TEXT NOT NULL,
    ano INTEGER,
    habitantes INTEGER,
    mortes_desastres INTEGER,
    pib_percapita INTEGER,
    gees_percapita INTEGER,
    desvio_media_temperatura INTEGER,
    energia_produzida INTEGER,
    energia_consumida INTEGER,
);
""")

con.execute("""
CREATE TABLE IF NOT EXISTS fontes (
    id INTEGER PRIMARY KEY,
    pais_id INTEGER NOT NULL,
    fonte TEXT,
    porcentagem INTEGER,
    FOREIGN KEY (pais_id) REFERENCES paises(id)
);
""")

# Fecha conexão
con.close()