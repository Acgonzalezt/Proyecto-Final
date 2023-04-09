CREATE_DW = '''
create table if not exists dimClientes(
    id_cliente INT primary key,
    nombre_del_cliente VARCHAR(100) UNIQUE,
    segmento VARCHAR(100),
    ciudad VARCHAR(100),
    estado VARCHAR(100),
    pais VARCHAR(100),
    region VARCHAR(100),
    gerente_regional VARCHAR(100)
);

CREATE table if not exists dimProducto(
    id_producto INT PRIMARY KEY,
    nombre_producto VARCHAR(100) UNIQUE,
    categoria VARCHAR(100),
    subcategoria VARCHAR(100)
);

CREATE table if not exists dimEnvio(
    id_forma_envio INT PRIMARY KEY,
    forma_envio VARCHAR(100)
);

create table if not exists dimCalendario(
	id_fecha varchar(50) primary key,
	year int,
	month int,
    day int,
	quarter int
);

CREATE TABLE IF NOT EXISTS Fact_Table(
     id_pedido INT PRIMARY KEY,
     id_cliente INT,
     id_producto INT,
     fecha_pedido DATE,
     fecha_envio DATE,
     id_forma_envio INT,
     ventas MONEY,
     cantidad INT,
     descuento MONEY,
     ganancia MONEY            
);
 '''