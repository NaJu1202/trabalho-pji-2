from mysql.connector import MySQLConnection


class ControlerVacinas:
    """Classe que representa o controlador de clientes"""

    def __init__(self, connection: MySQLConnection) -> None:
        """Inicializa o objeto ControlerCliente com uma conexão com o banco de dados"""
        self._connection = connection

    def pesquisar_vacinas_por_nome(self, nome_vacina: str) -> bool:
        """Pesquisar vacinas por nome"""
        try:
            pass
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao pesquisar vacinas por nome | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )

    def pesquisar_vacinas_por_país(self, nome_país: str) -> bool:
        """Pesquisar vacinas por país"""
        try:
            pass
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao pesquisar vacinas por país | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )

    def pesquisar_vacinas_por_continente(self, nome_continente: str) -> bool:
        """Pesquisar vacinas por continente"""
        try:
            pass
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao pesquisar vacinas por continente | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )
