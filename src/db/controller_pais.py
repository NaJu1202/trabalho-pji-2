from mysql.connector import MySQLConnection


class ControlerPais:
    """Classe que representa o controlador de clientes"""

    def __init__(self, connection: MySQLConnection) -> None:
        """Inicializa o objeto ControlerCliente com uma conexão com o banco de dados"""
        self._connection = connection

    def inserir_pais(self, nome_pais: str) -> None:
        """Inserir pais"""
        try:
            pass
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao inserir pais | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )

    def consultar_paises(self) -> tuple:
        """Consultar todos os paises cadastrados"""
        try:
            cursor = self._connection.cursor()
            cursor.execute("SELECT * FROM PAIS")
            return tuple(row[1] for row in cursor.fetchall())
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao consultar paises | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )
