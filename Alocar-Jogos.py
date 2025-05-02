modalidades_irreversivel = []

class Horario:
    def __init__(self, dia, hora_inicio, hora_fim):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.disponivel = True

    def conflito(self, outro_horario):
        if self.dia != outro_horario.dia:
            return False
        return not (self.hora_fim <= outro_horario.hora_inicio or self.hora_inicio >= outro_horario.hora_fim)

    def __repr__(self):
        return f"{self.dia} {self.hora_inicio}-{self.hora_fim}"

    def marcar_como_indisponivel(self):
        self.disponivel = False

    def proximo_horario(self):
        return Horario(self.dia, self.hora_fim, self.hora_fim + 1)

def verificar_disponibilidade_em_todas_secretarias(horario, categoria, secretarias_academicas):
    for secretaria in secretarias_academicas:
        for modalidade in secretaria.modalidades:
            if modalidade.categoria == categoria and modalidade.horario and modalidade.horario.conflito(horario):
                return False
    return True

class Secretaria_Academica:
    def __init__(self, nome):
        self.nome = nome
        self.modalidades = []
        self.horarios_disponiveis = []
        self.horarios_alocados = {'Feminino': set(), 'Masculino': set()}

    def adicionar_modalidade(self, modalidade):
        self.modalidades.append(modalidade)

    def adicionar_horario_disponivel(self, horario):
        self.horarios_disponiveis.append(horario)

    def esta_disponivel(self, horario):
        return horario.disponivel and all(not h.conflito(horario) for h in self.horarios_disponiveis)

    def resolver_conflito(self, modalidade, horario):
        categoria = modalidade.categoria
        for horario_alocado in self.horarios_alocados[categoria]:
            if horario.conflito(horario_alocado):
                print(f"Conflito detectado: {self.nome} já está alocada em {horario_alocado} para {categoria}.")
                return False
        
        self.horarios_alocados[categoria].add(horario)
        modalidade.horario = horario
        horario.marcar_como_indisponivel()
        return True
    
    def marcar_proximo_horario_indisponivel(self, horario, categoria):
        proximo_horario = horario.proximo_horario()
        proximo_horario.marcar_como_indisponivel()
        self.horarios_alocados[categoria].add(proximo_horario)

class Modalidade:
    def __init__(self, nome, horarios_permitidos, categoria, secretarias=[]):
        self.nome = nome
        self.horario = None
        self.categoria = categoria
        self.secretarias = secretarias
        self.horarios_permitidos = horarios_permitidos
        self.modalidade = nome.split(' ')[0]

    def alocar_secretarias_academicas(self):
        for horario in self.horarios_permitidos:
            # Restrições específicas
            if any(secretaria.nome in ['SAAero', 'SAPA', 'SAEMM', 'SAEComp'] for secretaria in self.secretarias):
                if horario.hora_inicio < 19:  # Restrição de horário: início após as 19h pois são do C2
                    continue

            # Restrições CCQ
            if any(secretaria.nome == 'CCQ' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições CEFiSC
            if any(secretaria.nome == 'CEFiSC' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições Pró-Produção
            if any(secretaria.nome == 'Pró-Produção' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SAAero
            if any(secretaria.nome == 'SAAero' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SAAU
            if any(secretaria.nome == 'SAAU' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SACEx
            if any(secretaria.nome == 'SACEx' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Sexta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Sexta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Sexta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Sexta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Sexta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Sexta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Sexta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Sexta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Sexta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Sexta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Sexta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Sexta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SACIM
            if any(secretaria.nome == 'SACIM' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SACivil
            if any(secretaria.nome == 'SACivil' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SAdEM
            if any(secretaria.nome == 'SAdEM' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SAEComp
            if any(secretaria.nome == 'SAEComp' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SAEMM
            if any(secretaria.nome == 'SAEMM' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SAMECA
            if any(secretaria.nome == 'SAMECA' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SAPA
            if any(secretaria.nome == 'SAPA' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições SA-SEL
            if any(secretaria.nome == 'SA-SEL' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            # Restrições Atlética
            if any(secretaria.nome == 'Atlética' for secretaria in self.secretarias):
                if self.modalidade == 'BM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'BF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'VF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCM' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FM' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'FF' and (
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HM' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quinta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quinta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quinta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'HF' and (
                    (horario.dia == 'Terca-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Terca-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Terca-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Terca-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue
                if self.modalidade == 'TCF' and (
                    (horario.dia == 'Segunda-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Segunda-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Segunda-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Segunda-Feira' and 21 <= horario.hora_inicio < 22) or 
                    (horario.dia == 'Quarta-Feira' and 18 <= horario.hora_inicio < 19) or 
                    (horario.dia == 'Quarta-Feira' and 19 <= horario.hora_inicio < 20) or 
                    (horario.dia == 'Quarta-Feira' and 20 <= horario.hora_inicio < 21) or 
                    (horario.dia == 'Quarta-Feira' and 21 <= horario.hora_inicio < 22)
                ):
                    continue

            if horario.disponivel and all(secretaria.esta_disponivel(horario) for secretaria in self.secretarias) and \
               verificar_disponibilidade_em_todas_secretarias(horario, self.categoria, self.secretarias):
                
                conflitos_detectados = False
                for secretaria in self.secretarias:
                    if not secretaria.resolver_conflito(self, horario):
                        conflitos_detectados = True
                        break
                
                if not conflitos_detectados:
                    for secretaria in self.secretarias:
                        secretaria.adicionar_modalidade(self)
                        secretaria.adicionar_horario_disponivel(horario)
                        secretaria.marcar_proximo_horario_indisponivel(horario, self.categoria)
                        
                    self.horario = horario
                    print(f"{self.nome} alocado em {horario}.")
                    return
        
        print(f"Não foi possível alocar {self.nome}. Conflito irreversível.")
        modalidades_irreversivel.append(self.nome)


def criar_secretarias_academicas(nomes):
    return [Secretaria_Academica(nome) for nome in nomes]

nomes_secretarias_academicas = ['SAAU', 'CCQ', 'CEFiSC', 'Pró-Produção', 'SAAero', 'SACEx', 'SACIM', 'SACivil', 'SAdEM', 'SAEComp', 'SAEMM', 'SAMECA', 'SA-SEL', 'SAPA']

# SAAU = 0
# CCQ = 1 
# CEFiSC = 2
# Pró-Produção = 3
# SAAero = 4
# SACEx = 5
# SACIM = 6
# SACivil = 7
# SAdEM = 8
# SAEComp = 9
# SAEMM = 10
# SAMECA = 11
# SA-SEL = 12
# SAPA = 13


secretarias_academicas = criar_secretarias_academicas(nomes_secretarias_academicas)

# BASQUETE Horarios
b1 = Horario('Segunda-Feira', 18, 19)
b2 = Horario('Segunda-Feira', 19, 20)
b3 = Horario('Segunda-Feira', 20, 21)
b4 = Horario('Segunda-Feira', 21,22)
b5 = Horario('Terca-Feira', 21, 22)
b6 = Horario('Quarta-Feira', 18, 19)
b7 = Horario('Quarta-Feira', 19, 20)
b8 = Horario('Quarta-Feira', 20,21)
b9 = Horario('Quarta-Feira', 21, 22)
b10 = Horario('Quinta-Feira', 21, 22)
b11 = Horario('Sexta-Feira', 18, 19)
b12 = Horario('Sexta-Feira', 19, 20)
b13 = Horario('Sexta-Feira', 20, 21)
b14 = Horario('Sexta-Feira', 21, 22)

horarios_permitidos_basquete= [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14]


# FUTSAL Horarios
f1 = Horario('Segunda-Feira', 18, 19)
f2 = Horario('Terca-Feira', 18, 19)
f3 = Horario('Terca-Feira', 19, 20)
f4 = Horario('Terca-Feira', 20, 21)
f5 = Horario('Terca-Feira', 21, 22)
f6 = Horario('Quarta-Feira', 20, 21)
f7 = Horario('Quarta-Feira', 21, 22)
f8 = Horario('Quinta-Feira', 18, 19)
f9 = Horario('Quinta-Feira', 19, 20)
f10 = Horario('Quinta-Feira', 20, 21)
f11 = Horario('Quinta-Feira', 21, 22)
f12 = Horario('Sexta-Feira', 18, 19)
f13 = Horario('Sexta-Feira', 19, 20)
f14 = Horario('Sexta-Feira', 20, 21)
f14 = Horario('Sexta-Feira', 21, 22)

horarios_permitidos_fut= [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14]

# HANDEBOL Horarios
h1 = Horario('Segunda-Feira', 18, 19)
h2 = Horario('Segunda-Feira', 19, 20)
h3 = Horario('Segunda-Feira', 20, 21)
h4 = Horario('Segunda-Feira', 21, 22)
h5 = Horario('Quarta-Feira', 18, 19)
h6 = Horario('Quarta-Feira', 19, 20)
h7 = Horario('Quarta-Feira', 20, 21)
h8 = Horario('Quarta-Feira', 21, 22)
h9 = Horario('Quinta-Feira', 21, 22)
h10 = Horario('Sexta-Feira', 18, 19)
h11 = Horario('Sexta-Feira', 19, 20)
h12 = Horario('Sexta-Feira', 20, 21)
h13 = Horario('Sexta-Feira', 21, 22)

horarios_permitidos_hand = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13]

# VOLEI horarios
v1 = Horario('Segunda-Feira', 18, 19)
v2 = Horario('Segunda-Feira', 19, 20)
v3 = Horario('Segunda-Feira', 20, 21)
v4 = Horario('Segunda-Feira', 21, 22)
v5 = Horario('Sexta-Feira', 18, 19)
v6 = Horario('Sexta-Feira', 19, 20)
v7 = Horario('Sexta-Feira', 20, 21)
v8 = Horario('Sexta-Feira', 21, 22)

horarios_permitidos_volei = [v1, v2, v3,v4, v5, v6, v7, v8]

#Jogos semana

# BASQUETE FEMININO
BF1 = Modalidade('BF – SAPA x SACIM', horarios_permitidos_basquete, 'Feminino', [secretarias_academicas[13], secretarias_academicas[6]])
BF1.alocar_secretarias_academicas()

BF2 = Modalidade('BF – SADEM x SAAERO', horarios_permitidos_basquete, 'Feminino', [secretarias_academicas[8], secretarias_academicas[4]])
BF2.alocar_secretarias_academicas()

BF3 = Modalidade('BF – SAMECA x PRO-PRODUÇÃO', horarios_permitidos_basquete, 'Feminino', [secretarias_academicas[11], secretarias_academicas[3]])
BF3.alocar_secretarias_academicas()

BF4 = Modalidade('BF – CCQ x SACIVIL', horarios_permitidos_basquete, 'Feminino', [secretarias_academicas[1], secretarias_academicas[7]])
BF4.alocar_secretarias_academicas()

# FUTSAL FEMININO
FF1 = Modalidade('FF – SACIM x PRO-PRODUÇÃO', horarios_permitidos_fut, 'Feminino', [secretarias_academicas[6], secretarias_academicas[3]])
FF1.alocar_secretarias_academicas()

FF2 = Modalidade('FF – CEFISC x SACEX', horarios_permitidos_fut, 'Feminino', [secretarias_academicas[2], secretarias_academicas[5]])
FF2.alocar_secretarias_academicas()

FF3 = Modalidade('FF – SAAERO x SAAU', horarios_permitidos_fut, 'Feminino', [secretarias_academicas[4], secretarias_academicas[0]])
FF3.alocar_secretarias_academicas()

FF4 = Modalidade('FF – SADEM x CCQ', horarios_permitidos_fut, 'Feminino', [secretarias_academicas[8], secretarias_academicas[1]])
FF4.alocar_secretarias_academicas()

# FUTSAL MASCULINO
FM1 = Modalidade('FM – SACIVIL x SA-SEL', horarios_permitidos_fut, 'Masculino', [secretarias_academicas[7], secretarias_academicas[12]])
FM1.alocar_secretarias_academicas()

FM2 = Modalidade('FM – SADEM x CCQ', horarios_permitidos_fut, 'Masculino', [secretarias_academicas[8], secretarias_academicas[1]])
FM2.alocar_secretarias_academicas()

FM3 = Modalidade('FM – SACEX x SAAU', horarios_permitidos_fut, 'Masculino', [secretarias_academicas[5], secretarias_academicas[0]])
FM3.alocar_secretarias_academicas()

FM4 = Modalidade('FM – PRO-PRODUCAO x SAAERO', horarios_permitidos_fut, 'Masculino', [secretarias_academicas[3], secretarias_academicas[4]])
FM4.alocar_secretarias_academicas()

# HANDEBOL FEMININO
HF1 = Modalidade('HF – CCQ x SACIVIL', horarios_permitidos_hand, 'Feminino', [secretarias_academicas[1], secretarias_academicas[7]])
HF1.alocar_secretarias_academicas()

HF2 = Modalidade('HF – SAMECA x SAAU', horarios_permitidos_hand, 'Feminino', [secretarias_academicas[11], secretarias_academicas[0]])
HF2.alocar_secretarias_academicas()

HF3 = Modalidade('HF – SACIM x PRO-PRODUÇÃO', horarios_permitidos_hand, 'Feminino', [secretarias_academicas[6], secretarias_academicas[3]])
HF3.alocar_secretarias_academicas()

HF4 = Modalidade('HF – SAEMM x SAAERO', horarios_permitidos_hand, 'Feminino', [secretarias_academicas[10], secretarias_academicas[4]])
HF4.alocar_secretarias_academicas()

# HANDEBOL MASCULINO
HM1 = Modalidade('HM – CCQ x SAAERO', horarios_permitidos_hand, 'Masculino', [secretarias_academicas[1], secretarias_academicas[4]])
HM1.alocar_secretarias_academicas()

HM2 = Modalidade('HM – CEFISC x SACIM', horarios_permitidos_hand, 'Masculino', [secretarias_academicas[2], secretarias_academicas[6]])
HM2.alocar_secretarias_academicas()

HM3 = Modalidade('HM – SAMECA x SACIVIL', horarios_permitidos_hand, 'Masculino', [secretarias_academicas[11], secretarias_academicas[7]])
HM3.alocar_secretarias_academicas()

# VÔLEI MASCULINO
VM1 = Modalidade('VM – SAPA x SACIM', horarios_permitidos_volei, 'Masculino', [secretarias_academicas[13], secretarias_academicas[6]])
VM1.alocar_secretarias_academicas()

VM2 = Modalidade('VM – SAAERO x SADEM', horarios_permitidos_volei, 'Masculino', [secretarias_academicas[4], secretarias_academicas[8]])
VM2.alocar_secretarias_academicas()

VM3 = Modalidade('VM – SA-SEL x SAECOMP', horarios_permitidos_volei, 'Masculino', [secretarias_academicas[12], secretarias_academicas[9]])
VM3.alocar_secretarias_academicas()

VM4 = Modalidade('VM – SAMECA x SACIVIL', horarios_permitidos_volei, 'Masculino', [secretarias_academicas[11], secretarias_academicas[7]])
VM4.alocar_secretarias_academicas()

VM5 = Modalidade('VM – PRO-PRODUÇÃO x SAAU', horarios_permitidos_volei, 'Masculino', [secretarias_academicas[3], secretarias_academicas[0]])
VM5.alocar_secretarias_academicas()

VM6 = Modalidade('VM – CEFISC x SAEMM', horarios_permitidos_volei, 'Masculino', [secretarias_academicas[2], secretarias_academicas[10]])
VM6.alocar_secretarias_academicas()

ordem_dias = {
    'Segunda-Feira': 1,
    'Terca-Feira': 2,
    'Quarta-Feira': 3,
    'Quinta-Feira': 4,
    'Sexta-Feira': 5,
    'Domingo': 6
}


def gerar_relatorio_e_agenda(secretarias_academicas):
    relatorio = ""
    # Usar um conjunto para garantir eventos únicos
    agenda = set() 
    
    for secretaria_academica in secretarias_academicas:
        relatorio += f"{secretaria_academica.nome}:\n"
        
        # Ordenar as modalidades pelo horário considerando a ordem dos dias
        modalidades_ordenadas = sorted(secretaria_academica.modalidades, key=lambda modalidade: (ordem_dias[modalidade.horario.dia], modalidade.horario.hora_inicio))
        
        for modalidade in modalidades_ordenadas:
            relatorio += f"  - {modalidade.nome}: {modalidade.horario}\n"
            agenda.add((modalidade.nome, modalidade.horario))

    agenda = list(agenda)
    agenda.sort(key=lambda x: (x[1].dia, x[1].hora_inicio, x[1].hora_fim))
    
    agenda_str = "Agenda de Jogos:\n"
    for modalidade, horario in agenda:
        agenda_str += f"{modalidade} - {horario}\n"
    
    return relatorio, agenda_str


relatorio, agenda_str = gerar_relatorio_e_agenda(secretarias_academicas)

with open("AGENDA-03-05-2025.txt", "w") as file:
    file.write("Relatório de Conflitos e Alocações:\n")
    file.write(relatorio)
    file.write("\n")
    file.write(agenda_str)
    file.write("\n")
    file.write("Jogos não alocados")
    file.write("\n")
    for modalidade in modalidades_irreversivel:
        file.write(modalidade)
        file.write("\n")

print("Relatório e agenda exportados para 'AGENDA-03-05-2025.txt'")
