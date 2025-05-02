function gerarRestricoesPython() {
    const planilha = SpreadsheetApp.getActiveSpreadsheet();
    const abas = planilha.getSheets();
  
    const diasSemana = ['Segunda-Feira', 'Terca-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira'];
    const horaInicioNumerica = [18, 19, 20, 21];
  
    const modalidades = [
      {nome: 'BM', linha: 9, coluna: 2},
      {nome: 'BF', linha: 16, coluna: 2},
      {nome: 'VM', linha: 23, coluna: 2},
      {nome: 'VF', linha: 30, coluna: 2},
      {nome: 'TCM', linha: 37, coluna: 2},
      {nome: 'FM', linha: 9, coluna: 9},
      {nome: 'FF', linha: 16, coluna: 9},
      {nome: 'HM', linha: 23, coluna: 9},
      {nome: 'HF', linha: 30, coluna: 9},
      {nome: 'TCF', linha: 37, coluna: 9},
    ];
  
    let codigoPython = "";
  
    abas.forEach(aba => {
      const nomeAba = aba.getName();
      const range = aba.getDataRange();
      const valores = range.getValues();
      const cores = range.getBackgrounds();
  
      const totalLinhas = valores.length;
      const totalColunas = valores[0].length;
  
      let restricoesPorModalidade = {};
  
      modalidades.forEach(mod => {
        let linhaDias = mod.linha;
        let linhaHorarios = mod.linha;
  
        for (let i = 0; i < 5; i++) {
          let colDia = mod.coluna + i;
          if (colDia >= totalColunas) continue;
  
          let dia = diasSemana[i];
  
          for (let j = 0; j < 4; j++) {
            let linhaAtual = linhaHorarios + j;
            if (linhaAtual >= totalLinhas) continue;
  
            let horaNum = horaInicioNumerica[j];
  
            let corCelula = cores[linhaAtual][colDia];
  
            Logger.log(
    `Modalidade: ${mod.nome}, Dia: ${dia}, Hora: ${horaNum}h, Linha: ${linhaAtual}, Coluna: ${colDia}, Cor: ${corCelula}`
  );
  
  
            if (corCelula.toLowerCase() != "#ffffff") {
              let cond = `(horario.dia == '${dia}' and ${horaNum} <= horario.hora_inicio < ${horaNum + 1})`;
              if (!restricoesPorModalidade[mod.nome]) {
                restricoesPorModalidade[mod.nome] = [];
              }
              restricoesPorModalidade[mod.nome].push(cond);
            }
          }
        }
      });
  
      // Gerar código Python
      codigoPython += `# Restrições ${nomeAba}\n`;
      codigoPython += `if any(secretaria.nome == '${nomeAba}' for secretaria in self.secretarias):\n`;
  
      for (let modalidade in restricoesPorModalidade) {
        let condicoes = restricoesPorModalidade[modalidade];
        codigoPython += `    if self.modalidade == '${modalidade}' and (\n`;
        codigoPython += `        ${condicoes.join(' or \n        ')}\n`;
        codigoPython += `    ):\n`;
        codigoPython += `        continue\n`;
      }
  
      codigoPython += `\n`;
    });
  
    const data = new Date().toISOString().slice(0,10); // '2025-04-07'
    const nomeArquivo = `restricoes_geradas_${data}.txt`;
    DriveApp.createFile(Utilities.newBlob(codigoPython, 'text/plain', nomeArquivo));
    Logger.log('Arquivo salvo no seu Google Drive!');
  
  }
  