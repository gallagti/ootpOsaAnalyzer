import csv
import sys
import re
file = open("PosStr_6-2-2061.csv", encoding="utf8")


def process_data():
    with open('PosStr_7-12-2061.csv', errors='ignore') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        team = []
        position = ["Catchers", "First Basemen", "Second Basemen", "Third Basemen", "Shortstops", "Leftfielders", "Centerfielders", "Rightfielders", "Starting Pitchers", "Relievers", "Closers"]
        top_player = []
        team_rank = []
        top_prospect = []
        org_rank = []
        ovr_rank = []
        lines = int(0)
        temp_line = int(0)
        for row in readCSV:
            if temp_line == 13:
                temp_line = 0
            if lines > 6 and row[0] == '':
                team.append(row[1])
                temp_line += 1
            elif lines > 6 and temp_line == 1:
                temp_line +=1
            elif lines > 6 and temp_line > 1:
                top_player.append(row[1])
                team_rank.append(row[2])
                top_prospect.append(row[3])
                org_rank.append(row[4])
                ovr_rank.append(row[5])
                temp_line+=1

            lines+=1
        i = int(0)
        return team, top_player, team_rank, top_prospect, org_rank, ovr_rank

def make_int(v):
    int_list = []
    for line in v:
        temp = ""
        for i in line:
            x = i
            if x.isdigit():
                temp = temp + x
                i = int(0)
        int_list.append(temp)
    return int_list


def main():
    posaverage = int(0)
    average = int(0)

    CRank = int(0)
    ProsCRank = int(0)
    IFAverage = int(0)
    OFAverage = int(0)
    oRank = int(0)
    MIFRank = int(0)
    MIFAvg = int(0)
    oRankAvg = int(0)
    SPRank = int(0)
    RPRank = int(0)
    PreemRank = int(0)
    ExpPreemRank = int(0)
    ProsAvgRank = int(0)
    ProsPosAvg = int(0)
    ProsInfRank = int(0)
    ProsOFRank = int(0)
    ProsSPRank = int(0)
    ProsRPRank = int(0)
    ProsPreemRank = int(0)
    count = int(0)

    teams = []
    position = ["Catchers", "First Basemen", "Second Basemen", "Third Basemen", "Shortstops", "Leftfielders",
                "Centerfielders", "Rightfielders", "Starting Pitchers", "Relievers", "Closers"]
    top_player = []
    team_rank = []
    top_prospect = []
    org_rank = []
    ovr_rank = []
    int_team_rank = []
    int_org_rank = []
    int_ovr_rank = []
    teams, top_player, team_rank, top_prospect, org_rank, ovr_rank = process_data()
    int_team_rank = make_int(team_rank)
    int_org_rank = make_int(org_rank)
    int_ovr_rank = make_int(ovr_rank)
    team_no = int(0)
    with open('PosStrResults_7-12-2061.csv', mode='w', newline='') as pos_file:
        writer = csv.writer(pos_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Team', 'Average Rank', 'Positional Average', 'Catcher Rank', 'Infield Average', 'OF Average',
                         'SP Rank', 'RP/CL AVG', 'Premium Position Rank (C/SS/CF)', 'Offense Rank(1B/3B/LF/RF)',
                         'Expanded Preem (SP/C/2B/SS/CF/RP)', 'MIF Avg'])
                        #,'Prospect Average Rank', 'Prospect Infield Rank', 'Prospect OF Rank', 'Prospect SP Rank', 'Prospect RP/CL Rank', 'Premium Pos. Rank'])
        for team in teams:
            posaverage = 0
            average = 0
            CRank = 0
            IFAverage = 0
            OFAverage = 0
            SPRank = 0
            RPRank = 0
            PreemRank = 0
            count = 0
            base_number = team_no*11
            if base_number != 352:
                for i in range(11):
                    count += int(int_team_rank[base_number + i])
                average = count/11
                CRank = int_team_rank[base_number + 0]
                count = 0

                for x in range(8):
                    count += int(int_team_rank[base_number + x])
                posaverage = count/8
                count = 0

                for q in range(1, 5):
                    count += int(int_team_rank[base_number + q])
                IFAverage = count/4
                count = 0

                for w in range(5, 8):
                    count += int(int_team_rank[base_number + w])
                OFAverage = count/3
                count = 0

                SPRank = int(int_team_rank[base_number + 8])
                for e in range(9, 11):
                    count += int(int_team_rank[base_number + e])
                RPRank = count/2
                count = 0

                PreemRank = (int(int_team_rank[base_number])+int(int_team_rank[base_number+4])+int(int_team_rank[base_number+6]))
                PreemAvg = PreemRank/3

                oRank = (int(int_team_rank[base_number+1]) + int(int_team_rank[base_number + 3]) + int(
                    int_team_rank[base_number + 5]) + int(int_team_rank[base_number + 7]))
                oRankAvg = int(oRank/4)
                count = 0
                ExpPreemRank = (int(int_team_rank[base_number]) + int(int_team_rank[base_number +2]) + int(
                    int_team_rank[base_number + 4]) + int(int_team_rank[base_number + 6])+ int(int_team_rank[base_number + 8])+ RPRank)
                count = ExpPreemRank/6
                MIFRank = int(int_team_rank[base_number+2]) + int(int_team_rank[base_number +4])
                MIFAvg = MIFRank/2

                writer.writerow([team, average, posaverage, CRank, IFAverage, OFAverage, SPRank, RPRank, PreemAvg, oRankAvg, count, MIFAvg])
                team_no +=1
        team_no = 0
        writer.writerow(['Prospects'])
        for team in teams:
            ProsAvgRank = 0
            ProsPosAvg = 0
            ProsInfRank = 0
            ProsCRank = 0
            ProsOFRank = 0
            ProsSPRank = 0
            ProsRPRank = 0
            ProsPreemRank = 0
            count = 0
            base_number = team_no * 11
            if base_number != 352:
                for i in range(11):
                    count += int(int_org_rank[base_number + i])
                ProsAvgRank = count / 11
                ProsCRank = int_org_rank[base_number + 0]
                count = 0

                for x in range(8):
                    count += int(int_org_rank[base_number + x])
                ProsPosAvg = count / 8
                count = 0

                for q in range(1, 5):
                    count += int(int_org_rank[base_number + q])
                ProsInfRank = count / 4
                count = 0

                for w in range(5, 8):
                    count += int(int_org_rank[base_number + w])
                ProsOFRank = count / 3
                count = 0

                ProsSPRank = int(int_org_rank[base_number + 8])
                for e in range(9, 11):
                    count += int(int_org_rank[base_number + e])
                ProsRPRank = count / 2
                count = 0

                ProsPreemRank = (int(int_org_rank[base_number]) + int(int_org_rank[base_number + 4]) + int(
                    int_org_rank[base_number + 6]))
                PreemAvg = ProsPreemRank / 3
                writer.writerow([team, ProsAvgRank, ProsPosAvg, ProsCRank, ProsInfRank, ProsOFRank, ProsSPRank, ProsRPRank, PreemAvg])
                team_no += 1

    return 0

if __name__ == "__main__":
    main()