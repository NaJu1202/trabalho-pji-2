CREATE TABLE continentes (
    id_continente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE paises (
    id_pais INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL UNIQUE,
    id_continente INT NOT NULL,
    FOREIGN KEY (id_continente) REFERENCES continentes(id_continente)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE vacinas_obrigatorias_viagem (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_pais INT NOT NULL,
    nome_vacina VARCHAR(150) NOT NULL,
    grupo_de_risco VARCHAR(200),
    FOREIGN KEY (id_pais) REFERENCES paises(id_pais)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
