from mysql.connector import MySQLConnection


class ControlerContinente:
    """Classe que representa o controlador de clientes"""

    def __init__(self, connection: MySQLConnection) -> None:
        """Inicializa o objeto ControlerCliente com uma conexão com o banco de dados"""
        self._connection = connection

    def consultar_continentes(self) -> bool:
        """Inserir continente"""
        try:
            pass
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao inserir continente | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )
