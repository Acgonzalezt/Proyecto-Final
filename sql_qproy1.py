DDL_QUERY =  '''

CREATE TABLE IF NOT EXISTS ventas(
    id_de_la_fila INT,
    id_pedido INT PRIMARY KEY,
    fecha_pedido DATE,
    fecha_envio DATE,
    forma_envio VARCHAR(100),
    id_cliente INT,
    nombre_del_cliente VARCHAR(100),
    segmento VARCHAR(100),
    ciudad VARCHAR(100),
    estado VARCHAR(100),
    pais_region VARCHAR(100),
    region VARCHAR(100),
    id_producto INT,
    categoria VARCHAR(100),
    subcategoria VARCHAR(100),
    nombre_producto VARCHAR(100),
    ventas DOUBLE PRECISION,
    cantidad INT,
    descuento DOUBLE PRECISION,
    ganancia DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS personas(
    id_gerente SERIAL PRIMARY KEY,
    region VARCHAR(100),
    gerente_regional VARCHAR(100)

);

SELECT * FROM ventas;
SELECT * FROM personas; '''