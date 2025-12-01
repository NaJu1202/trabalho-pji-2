import sqlite3
from sqlite3 import Connection

from src.db.controller_continente import ControlerContinente
from src.db.controller_pais import ControlerPais
from src.db.controller_vacinas import ControlerVacinas


class ConnectionDB:
    """
    Classe que gerencia a conexão com o banco SQLite (.db)
    e seus controllers.
    """

    def __init__(self, db_path: str = "labdatabase.db") -> None:
        self.db_path = db_path

        self.__connection: Connection | None = None
        self.__controler_vacinas: ControlerVacinas | None = None
        self.__controler_pais: ControlerPais | None = None
        self.__controler_continente: ControlerContinente | None = None

    @property
    def conection(self) -> Connection:
        """
        Retorna a conexão com o banco SQLite.
        Cria a conexão se ainda não existir.
        """

        try:
            if self.__connection is None:
                # Abre o arquivo .db (cria automaticamente se não existir)
                self.__connection = sqlite3.connect(
                    self.db_path,
                    check_same_thread=False,  # importante para APIs e Streamlit
                )
                # Retornar linhas como dicionário
                self.__connection.row_factory = sqlite3.Row

            return self.__connection

        except Exception as e:
            raise Exception(f"Erro ao conectar ao banco SQLite | {str(e)}")

    def fechar_conexao(self) -> None:
        """Fecha a conexão com o banco SQLite"""
        try:
            if self.__connection:
                self.__connection.close()

            self.__connection = None
            self.__controler_vacinas = None
            self.__controler_pais = None
            self.__controler_continente = None

        except Exception as e:
            raise Exception(f"Erro ao fechar conexão SQLite | {str(e)}")

    @property
    def controler_vacinas(self) -> ControlerVacinas:
        """Retorna o controller de vacinas"""
        try:
            if self.__controler_vacinas is None:
                self.__controler_vacinas = ControlerVacinas(connection=self.conection)
            return self.__controler_vacinas
        except Exception as e:
            raise Exception(f"Erro ao iniciar controller vacinas | {str(e)}")

    @property
    def controler_pais(self) -> ControlerPais:
        """Retorna o controller de países"""
        try:
            if self.__controler_pais is None:
                self.__controler_pais = ControlerPais(connection=self.conection)
            return self.__controler_pais
        except Exception as e:
            raise Exception(f"Erro ao iniciar controller país | {str(e)}")

    @property
    def controler_continente(self) -> ControlerContinente:
        """Retorna o controller de continentes"""
        try:
            if self.__controler_continente is None:
                self.__controler_continente = ControlerContinente(
                    connection=self.conection
                )
            return self.__controler_continente
        except Exception as e:
            raise Exception(f"Erro ao iniciar controller continente | {str(e)}")
