import os

import mysql.connector
from mysql.connector import MySQLConnection

from src.db.controller_continente import ControlerContinente
from src.db.controller_pais import ControlerPais
from src.db.controller_vacinas import ControlerVacinas


class ConnectionDB:
    """Classe que gerencia a conexão com o banco de dados e seus controllers"""

    def __init__(self) -> None:
        """Inicia o objeto da classe de conexão com o banco de dados"""
        self.__conection: MySQLConnection | None = None
        self.__controler_vacinas: ControlerVacinas | None = None
        self.__controler_pais: ControlerPais | None = None
        self.__controler_continente: ControlerContinente | None = None

    @property
    def conection(self) -> MySQLConnection:
        """Retorna a conexão com o banco, criando ou reconectando se necessário."""
        try:
            if self.__conection is None:
                self.__conection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="mysql",
                    database="labdatabase",
                )

            elif not self.__conection.is_connected():
                try:
                    self.__conection.reconnect(attempts=3, delay=2)
                except Exception:
                    self.__conection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="mysql",
                        database="labdatabase",
                    )

            return self.__conection
        except Exception as e:
            raise Exception(f"Erro ao realizar conexão com o banco de dados | {str(e)}")

    def fechar_conexao(self) -> None:
        """Fecha a conexão com o banco"""
        try:
            if self.__conection and self.__conection.is_connected():
                self.__conection.close()
            self.__conection = None
            self.__controler_vacinas = None
            self.__controler_pais = None
            self.__controler_continente = None
        except Exception as e:
            raise Exception(f"Erro ao fechar conexão com o banco de dados | {str(e)}")

    @property
    def controler_vacinas(self) -> ControlerVacinas:
        """Retorna o controller de vacinas"""
        try:
            if self.__controler_vacinas is None:
                self.__controler_vacinas = ControlerVacinas(connection=self.conection)
            return self.__controler_vacinas
        except Exception as e:
            raise Exception(f"Erro ao iniciar controller clientes | {str(e)}")

    @property
    def controler_pais(self) -> ControlerPais:
        """Retorna o controller de pais"""
        try:
            if self.__controler_pais is None:
                self.__controler_pais = ControlerPais(connection=self.conection)
            return self.__controler_pais
        except Exception as e:
            raise Exception(f"Erro ao iniciar controller pais | {str(e)}")

    @property
    def controler_continente(self) -> ControlerContinente:
        """Retorna o controller de continente"""
        try:
            if self.__controler_continente is None:
                self.__controler_continente = ControlerContinente(
                    connection=self.conection
                )
            return self.__controler_continente
        except Exception as e:
            raise Exception(f"Erro ao iniciar controller continente | {str(e)}")
