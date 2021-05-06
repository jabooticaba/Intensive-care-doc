Sub print3()
'
' print3 macro
'

'
    Sheets("карта ИТ").Select
    ActiveWindow.SelectedSheets.PrintOut Copies:=1, Collate:=True, _
        IgnorePrintAreas:=False
    Sheets("назначения").Select
    ActiveWindow.SelectedSheets.PrintOut Copies:=1, Collate:=True, _
        IgnorePrintAreas:=False
    ActiveWindow.ScrollWorkbookTabs Sheets:=1
    ActiveWindow.ScrollWorkbookTabs Sheets:=1
    ActiveWindow.ScrollWorkbookTabs Sheets:=1
    Sheets("на кровать").Select
    ActiveWindow.SelectedSheets.PrintOut Copies:=1, Collate:=True, _
        IgnorePrintAreas:=False
    Sheets("согласия").Select
    ActiveWindow.SelectedSheets.PrintOut From:=1, To:=6, Copies:=1, Collate _
        :=True, IgnorePrintAreas:=False
    Sheets("разовые").Select
    Application.Dialogs(xlDialogPrint).Show
End Sub
