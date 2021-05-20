class pessoa:
    def __init__(self,nome,dataNascimento,endereco):
        self.nome=nome
        self.dataNascimento=dataNascimento
        self.endereco=endereco

class aluno(pessoa):
    def __init__(self,nome,dataNascimento,endereco,cd_Matricula,curso,nota1,nota2,nota3):
        super().__init__(nome,dataNascimento,endereco)
        self.cd_Matricula=cd_Matricula
        self.curso=curso
        self.soma=nota1+nota2+nota3
        self.media=(self.soma)/3
    def responder_chamada(self,presenca):
        self.presenca=presenca
        

class professor(pessoa):
    def __init__(self,nome,dataNascimento,endereco,cd_Funcionario,curso,disciplina):
        super().__init__(nome,dataNascimento,endereco)
        self.cd_Funcionario=cd_Funcionario
        self.curso=curso
        self.disciplina=disciplina

    def method_chamada(self,Realdo,Otavio):
        chamada=Realdo.nome+": "+Realdo.presenca+"\n"
        chamada+=Otavio.nome+": "+Otavio.presenca+"\n"
        print(chamada)

Realdo=aluno("Realdo","25/04/03","Turvo",46643,"Informatica",10,2,5)
Otavio=aluno("Otavio","13/07/04","Timbe",46687,"Quimica",10,9,5)
Cris=professor("Cris","23/09/89","Criciuma",76234,"Informatica","MySQL")


Realdo.responder_chamada("Presente")
Otavio.responder_chamada("Ausente")
Cris.method_chamada(Realdo,Otavio)



print("\nAluno: ",Realdo.nome,"\nData de nascimento: ",Realdo.dataNascimento,"\nEndereço: ",Realdo.endereco,"\nMatricula: ",Realdo.cd_Matricula,"\nCurso: ",Realdo.curso,"\nMedia: ",Realdo.media)
print("\n\n")
print("Aluno: ",Otavio.nome,"\nData de nascimento: ",Otavio.dataNascimento,"\nEndereço: ",Otavio.endereco,"\nMatricula: ",Otavio.cd_Matricula,"\nCurso: ",Otavio.curso,"\nMedia: ",Otavio.media)
print("\n\n")
print("Professor: ",Cris.nome,"\nData de nascimento: ",Cris.dataNascimento,"\nEndereço: ",Cris.endereco,"\nFuncionario: ",Cris.cd_Funcionario,"\nCurso: ",Cris.curso,"\nDisciplina: ",Cris.disciplina)
