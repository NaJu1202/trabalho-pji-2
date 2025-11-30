import pandas as pd
from mysql.connector import MySQLConnection


class ControlerVacinas:
    """Classe que representa o controlador de clientes"""

    def __init__(self, connection: MySQLConnection) -> None:
        """Inicializa o objeto ControlerCliente com uma conexão com o banco de dados"""
        self._connection = connection

    def consultar_vacinas(self) -> tuple:
        """Consultar todos as vacinas cadastradas"""
        try:
            cursor = self._connection.cursor()
            cursor.execute("SELECT * FROM VACINAS_OBRIGATORIAS_VIAGEM")
            return tuple(row[2] for row in cursor.fetchall())
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao consultar vacinas | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )

    def pesquisar_vacinas_por_nome(self, nome_vacina: str) -> bool:
        """Pesquisar vacinas por nome"""
        try:
            consulta = f"""SELECT * 
            FROM VACINAS_OBRIGATORIAS_VIAGEM 
            WHERE NOME_VACINA LIKE '%{nome_vacina}%'"""

            df = pd.read_sql(consulta, self._connection)

            df.drop(columns=["ID_PAIS"], inplace=True)

            return df
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao pesquisar vacinas por nome | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )

    def pesquisar_vacinas_por_país(self, nome_país: str) -> bool:
        """Pesquisar vacinas por país"""
        try:
            consulta = f"""SELECT * 
            FROM VACINAS_OBRIGATORIAS_VIAGEM
            WHERE ID_PAIS = (SELECT ID_PAIS FROM PAISES WHERE NOME = '{nome_país}')
            """

            df = pd.read_sql(consulta, self._connection)

            df.drop(columns=["ID_PAIS"], inplace=True)
            df.drop(columns=["ID"], inplace=True)

            

            return df
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao pesquisar vacinas por país | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )

    def pesquisar_vacinas_por_continente(self, nome_continente: str) -> bool:
        """Pesquisar vacinas por continente"""
        try:
            consulta = f"""
            SELECT v.id_pais,
                p.nome AS pais,
                c.nome AS continente,
                v.nome_vacina,
                v.grupo_de_risco
            FROM VACINAS_OBRIGATORIAS_VIAGEM v
            JOIN PAISES p ON p.id_pais = v.id_pais
            JOIN CONTINENTES c ON c.id_continente = p.id_continente
            WHERE c.nome = '{nome_continente}'
            """

            df = pd.read_sql(consulta, self._connection)

            df.drop(columns=["ID_PAIS"], inplace=True)

            return df
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao pesquisar vacinas por continente | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )
