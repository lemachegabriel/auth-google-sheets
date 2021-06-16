
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(creds)
sheet = client.open("users").sheet1
i=2
date_today = sheet.cell(4,8).value
arquivo = open("nao_apagar", "r+")
mytoken = arquivo.readline(15)
new_val = sheet.cell(2,7).value

while(True):    
    date_val = sheet.cell(i,3).value
    ids = sheet.cell(i,1).value
    curr_token = sheet.cell(i,2).value
    
    if ids == None:
        print('Id incorreto')
        break
    if ids == self.id:
        if (curr_token == mytoken or curr_token != mytoken) and date_today >= date_val:
            new_token = self.token(15)
            file = glob.glob('*nao_apagar')
            for files in file:
                arquivo.close()
                os.unlink(files)
            new_arquivo = open("nao_apagar", "w+")
            new_arquivo.write(new_token)
            new_arquivo.close()
            sheet.update_cell(i,2, new_token)
            sheet.update_cell(i,3, new_val)
            self.login()
        elif curr_token == mytoken and date_today < date_val:
            self.login()
        elif curr_token != mytoken and date_today < date_val:
            print('Essa conta ja está em uso')
            break 
    i+=1       