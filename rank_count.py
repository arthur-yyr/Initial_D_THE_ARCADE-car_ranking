import course_url
import json
import xlsxwriter
import os

def rank_count():
    if os.path.exists("Initial_D.xlsx"):
        os.remove("Initial_D.xlsx")
    workbook = xlsxwriter.Workbook("Initial_D.xlsx")
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})
    global_car_freq = dict()
    for i in range(0, course_url.course_list_len):
        course = course_url.course_list[i][0]
        
        with open("courses/" + course + ".json", "r") as f:
            worksheet = workbook.add_worksheet(course)
            # Record top1 player's data
            course_data = json.load(f)
            last_update = "JST " + course_data["calcDate"]
            top1_data = course_data["records"][0]
            top1_data.pop("mytitleId")
            top1_data = {k:[v] for k,v in top1_data.items()}
            
            # Dict is sorted by appeared rank
            top_used_car_rank = dict()
            for rank_data in course_data["records"]:
                carname = rank_data["carname"]
                if carname in top_used_car_rank:
                    top_used_car_rank[carname] += 1
                else:
                    top_used_car_rank[carname] = 1

                if carname in global_car_freq:
                    global_car_freq[carname] += 1
                else:
                    global_car_freq[carname] = 1

            # List is sorted by freq
            top_used_car_freq = top_used_car_rank.items()
            top_used_car_freq = sorted(top_used_car_freq, key=lambda x: x[1], reverse=True)
            
            # Write data
            worksheet.write('A1', "コース：", bold)
            worksheet.write('B1', course)
            worksheet.write('D1', "資料更新：", bold)
            worksheet.write('E1', last_update)
            worksheet.write('G1', "ランキング1のデータ：", bold)
            worksheet.write('H1', "ドライバー名：")
            worksheet.write('I1', top1_data['name'][0])
            worksheet.write('H2', "所属店舗：",)
            worksheet.write('I2', top1_data['shopname'][0])
            worksheet.write('H3', "レコード：")
            worksheet.write('I3', top1_data['record'][0])
            worksheet.write('H4', "レコード時間：", )
            worksheet.write('I4', top1_data['updateDate'][0])
            worksheet.write('H5', "車種：")
            worksheet.write('I5', top1_data['carname'][0])
            worksheet.write('A3', "TOP1000の車（ランキング順）：", bold)
            worksheet.write('A4', "車種", bold)
            worksheet.write('B4', "頻度", bold)
            row = 5
            for car, freq in top_used_car_rank.items():
                worksheet.write('A'+str(row), car)
                worksheet.write('B'+str(row), freq)
                row += 1
                
            worksheet.write('D3', "TOP1000の車（頻度順）：", bold)
            worksheet.write('D4', "車種", bold)
            worksheet.write('E4', "頻度", bold)
            row = 5
            for car_freq in top_used_car_freq:
                worksheet.write('D'+str(row), car_freq[0])
                worksheet.write('E'+str(row), car_freq[1])
                row += 1
           
    global_car_freq = global_car_freq.items()
    global_car_freq = sorted(global_car_freq, key=lambda x: x[1], reverse=True)
    worksheet = workbook.add_worksheet("全て")
    worksheet.write('A1', "車種", bold)
    worksheet.write('B1', "頻度", bold)
    row = 2
    for car, freq in global_car_freq:
        worksheet.write('A'+str(row), car)
        worksheet.write('B'+str(row), freq)
        row += 1
    
    workbook.close()

if __name__ == "__main__":
    rank_count()
    print("\nFile Created.\n")