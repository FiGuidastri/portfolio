let
    Fonte = Table.FromRecords({  // Este é apenas um exemplo de uma tabela fato
        [DataInicial = #date(2023, 1, 1), Valor = 100],
        [DataInicial = #date(2023, 12, 31), Valor = 200]
    }),
    
    DataMinima = List.Min(Fonte[DataInicial]),
    DataMaxima = List.Max(Fonte[DataInicial]),
    
    QtdeDias = Duration.From(DataMaxima - DataMinima) + #duration(1, 0, 0, 0), // Adiciona 1 dia à duração

    ListaDatas = List.Dates(DataMinima, Number.From(QtdeDias), #duration(1, 0, 0, 0)),
    TabelaDatas = Table.FromList(ListaDatas, Splitter.SplitByNothing()),
    RenomeiaColunas = Table.RenameColumns(TabelaDatas,{{"Column1", "Data"}})
in
    RenomeiaColunas
