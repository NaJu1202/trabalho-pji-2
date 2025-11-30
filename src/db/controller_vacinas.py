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
            df.drop(columns=["ID"], inplace=True)

            df.rename(
                columns={
                    "NOME_VACINA": "Nome da Vacina",
                    "GRUPO_DE_RISCO": "Grupo de Risco",
                },
                inplace=True,
            )

            return df
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao pesquisar vacinas por nome | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )

    def pesquisar_vacinas_por_país(
        self, nome_país: str
    ) -> tuple[pd.DataFrame | None, bool]:
        """Pesquisar vacinas por país"""
        try:
            consulta = f"""SELECT * 
            FROM VACINAS_OBRIGATORIAS_VIAGEM
            WHERE ID_PAIS = (SELECT ID_PAIS FROM PAISES WHERE NOME = '{nome_país}')
            """

            df = pd.read_sql(consulta, self._connection)

            if df.empty:
                return None, False

            df.drop(columns=["ID_PAIS"], inplace=True)
            df.drop(columns=["ID"], inplace=True)

            df.rename(
                columns={
                    "NOME_VACINA": "Nome da Vacina",
                    "GRUPO_DE_RISCO": "Grupo de Risco",
                },
                inplace=True,
            )

            return df.to_dict("records"), True
        except Exception as e:
            self._connection.rollback()
            raise Exception(
                f"Ocorreu um erro inesperado ao pesquisar vacinas por país | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )

    def cadastrar_vacina(
        self, nome_vacina: str, grupo_de_risco: str, pais: str
    ) -> bool:
        """Inserir vacina"""
        try:
            cursor = self._connection.cursor()

            cursor.execute(
                "SELECT ID_PAIS FROM PAISES WHERE NOME = %s",
                (pais,),
            )

            id_pais = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO VACINAS_OBRIGATORIAS_VIAGEM (NOME_VACINA, GRUPO_DE_RISCO, ID_PAIS) VALUES (%s, %s, %s)",
                (nome_vacina, grupo_de_risco, id_pais),
            )
            self._connection.commit()
            return True
        except Exception as e:
            self._connection.rollback()
            print(
                f"Ocorreu um erro inesperado ao inserir vacina | Linha: {e.__traceback__.tb_lineno} | {str(e)}"
            )
            return False
