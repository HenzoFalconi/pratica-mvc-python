from model.database import Database

class tarefa:
    def __init__(self, id, titulo, data_conclusão):
        self.id = id
        self.titulo = titulo
        self.data_conclusão = data_conclusão
        pass

    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusão) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusão)
        db.executar(sql, params)
        db.desconectar()
        ]
    def listarTarefas(self):
        """Retorna uma lista de tarefas cadastradas."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusão FROM tarefa'  
        tarefas = db.consultar(sql)
        db.desconectar()

        return tarefas