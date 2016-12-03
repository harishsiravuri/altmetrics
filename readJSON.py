#############################################################################################################################
# Author: Harish Varma Siravuri                                                                                             #                             *
#                                                                                                                           #
#                                                                                                                           #
#                                                                                                                           #
#                                                                                                                           #
#                                                                                                                           #
#                                                                                                                           #
#############################################################################################################################
import csv
import os
import json
import numpy as np
from pprint import pprint

root_path= 'C:\\Users\\haris\\Documents\\697\\massive dataset\\data\\'
dump_path= "C:\\Users\\haris\\Desktop\\10\\sampled.csv"

with open(dump_path,'w') as sampledfile:
    datawriter=csv.writer(sampledfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['altmetric_id','mendeley_readers','citeulikereaders','connoteareaders','blog_users','blogs_posts_count','news_unique_users','total_posts_count','wiki_posts_count','facebook_users','facebook_posts','twitter_users','twitter_posts','citation_page','other_articles','mean','rank','perc','scored_higher_than','sample_size','users_lecturer','users_librarian','users_student_bachelor','users_student_master','users_student_pg','users_student_phd','users_student_doct','users_researcher','users_other','users_prof_assoc','users_prof','users_medi','users_ss','users_psych','users_earth','users_agri','users_arts','users_us','users_th','users_ie','users_id','users_au','users_gb','altmetric_score','altmetric_score_1y','altmetric_score_6m','altmetric_score_3m','altmetric_score_1m','altmetric_score_1w','altmetric_score_6d','altmetric_score_5d','altmetric_score_4d','altmetric_score_3d','altmetric_score_3d','altmetric_score_1d'])    
    for dirname in os.listdir(root_path):
        subdir_path=root_path+dirname+'\\'
        for filename in os.listdir(subdir_path):
            file_path=subdir_path+filename
            if(file_path[-4:]=='json'):
                with open(file_path) as json_data:
                    count=0
                    data=json.load(json_data)
                    if 'altmetric_id' in data:
                        altmetric_id=data['altmetric_id']
                        if 'readers' in data['counts'] and 'mendeley' in data['counts']['readers'] and isinstance(data['counts']['readers']['mendeley'], int):
                            mendeley_readers=data['counts']['readers']['mendeley']
                            count+=1
                        else:
                            mendeley_readers=0
                        if 'readers' in data['counts'] and 'citeulike' in data['counts']['readers'] and isinstance(data['counts']['readers']['citeulike'], int):
                            citeulikereaders=data['counts']['readers']['citeulike']
                            count+=1
                        else:
                            citeulikereaders=0
                        if 'readers' in data['counts'] and 'connotea' in data['counts']['readers'] and isinstance(data['counts']['readers']['connotea'], int):
                            connoteareaders=data['counts']['readers']['connotea']
                            count+=1
                        else:
                            connoteareaders=0
                        if 'blogs' in data['counts'] and 'unique_users_count' in data['counts']['blogs'] and isinstance(data['counts']['blogs']['unique_users_count'], int):
                            blog_users=data['counts']['blogs']['unique_users_count']
                            count+=1
                        else:
                            blog_users=0
                        if 'blogs' in data['counts'] and 'posts_count' in data['counts']['blogs'] and isinstance(data['counts']['blogs']['posts_count'], int):
                            blogs_posts_count=data['counts']['blogs']['posts_count']
                            count+=1
                        else:
                            blogs_posts_count=0
                        if 'news' in data['counts'] and isinstance(data['counts']['news']['unique_users_count'], int):
                            news_unique_users=data['counts']['news']['unique_users_count']
                            count+=1
                        else:
                            news_unique_users=0
                        if 'posts_count' in data['counts']['total'] and isinstance(data['counts']['total']['posts_count'], int):
                            total_posts_count=data['counts']['total']['posts_count']
                            count+=1
                        else:
                            total_posts_count=0
                        if 'wikipedia' in data['counts'] and isinstance(data['counts']['wikipedia']['unique_users_count'], int):
                            wiki_posts_count=data['counts']['wikipedia']['unique_users_count']
                            count+=1
                        else:
                            wiki_posts_count=0
                        if 'startpage' in data['citation'] and isinstance(data['citation']['startpage'], int):
                            citation_page=data['citation']['startpage']
                            count+=1
                        else:
                            citation_page=0
                        if 'facebook' in data['counts'] and 'unique_users_count' in data['counts']['facebook']:
                            facebook_users=data['counts']['facebook']['unique_users_count']
                        else:
                            facebook_users=0
                        if 'facebook' in data['counts'] and 'posts_count' in data['counts']['facebook']:
                            facebook_posts=data['counts']['facebook']['posts_count']
                        else:
                            facebook_posts=0
                        if 'twitter' in data['counts'] and 'unique_users_count' in data['counts']['twitter']:
                            twitter_users=data['counts']['twitter']['unique_users_count']
                        else:
                            twitter_users=0
                        if 'twitter' in data['counts'] and 'posts_count' in data['counts']['twitter']:
                            twitter_posts=data['counts']['twitter']['posts_count']
                        else:
                            twitter_posts=0
                        altmetric_score=data['altmetric_score']['score']
                        altmetric_score_1y=data['altmetric_score']['score_history']['1y']
                        altmetric_score_6m=data['altmetric_score']['score_history']['6m']
                        altmetric_score_3m=data['altmetric_score']['score_history']['3m']
                        altmetric_score_1m=data['altmetric_score']['score_history']['1m']
                        altmetric_score_1w=data['altmetric_score']['score_history']['1w']
                        altmetric_score_6d=data['altmetric_score']['score_history']['6d']
                        altmetric_score_5d=data['altmetric_score']['score_history']['5d']
                        altmetric_score_4d=data['altmetric_score']['score_history']['4d']
                        altmetric_score_3d=data['altmetric_score']['score_history']['3d']
                        altmetric_score_1d=data['altmetric_score']['score_history']['1d']
                        if data['altmetric_score']['context_for_score']!=None and 'total_number_of_other_articles' in data['altmetric_score']['context_for_score']['all'] and isinstance(data['altmetric_score']['context_for_score']['all']['total_number_of_other_articles'], int):
                            other_articles=data['altmetric_score']['context_for_score']['all']['total_number_of_other_articles']
                            count+=1
                        else:
                            other_articles=0
                        if data['altmetric_score']['context_for_score']!=None and 'mean' in data['altmetric_score']['context_for_score']['all']:
                            mean=data['altmetric_score']['context_for_score']['all']['mean']
                            count+=1
                        else:
                            mean=0
                        if data['altmetric_score']['context_for_score']!=None and 'rank' in data['altmetric_score']['context_for_score']['all']:
                            rank=data['altmetric_score']['context_for_score']['all']['rank']
                            count+=1
                        else:
                            rank=0
                        if data['altmetric_score']['context_for_score']!=None and 'this_scored_higher_than_pct' in data['altmetric_score']['context_for_score']['all']:
                            perc=data['altmetric_score']['context_for_score']['all']['this_scored_higher_than_pct']
                            count+=1
                        else:
                            perc=0
                        if data['altmetric_score']['context_for_score']!=None and 'this_scored_higher_than' in data['altmetric_score']['context_for_score']['all']:
                            scored_higher_than=data['altmetric_score']['context_for_score']['all']['this_scored_higher_than']
                            count+=1
                        else:
                            scored_higher_than=0
                        if data['altmetric_score']['context_for_score']!=None and 'sample_size' in data['altmetric_score']['context_for_score']['all']:
                            sample_size=data['altmetric_score']['context_for_score']['all']['sample_size']
                            count+=1
                        else:
                            sample_size=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Librarian' in data['demographics']['users']['mendeley']['by_status']:
                            users_librarian=data['demographics']['users']['mendeley']['by_status']['Librarian']
                            count+=1
                        else:
                            users_librarian=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Lecturer' in data['demographics']['users']['mendeley']['by_status']:
                            users_lecturer=data['demographics']['users']['mendeley']['by_status']['Lecturer']
                            count+=1
                        else:
                            users_lecturer=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student > Bachelor' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_bachelor=data['demographics']['users']['mendeley']['by_status']['Student  > Bachelor']
                            count+=1
                        else:
                            users_student_bachelor=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student > Master' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_master=data['demographics']['users']['mendeley']['by_status']['Student  > Master']
                            count+=1
                        else:
                            users_student_master=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student > Postgraduate' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_pg=data['demographics']['users']['mendeley']['by_status']['Student  > Postgraduate']
                            count+=1
                        else:
                            users_student_pg=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student  > Ph. D. Student' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_phd=data['demographics']['users']['mendeley']['by_status']['Student  > Ph. D. Student']
                            count+=1
                        else:
                            users_student_phd=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Student  > Doctoral Student' in data['demographics']['users']['mendeley']['by_status']:
                            users_student_doct=data['demographics']['users']['mendeley']['by_status']['Student  > Doctoral Student']
                            count+=1
                        else:
                            users_student_doct=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Researcher' in data['demographics']['users']['mendeley']['by_status']:
                            users_researcher=data['demographics']['users']['mendeley']['by_status']['Researcher']
                            count+=1
                        else:
                            users_researcher=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Other' in data['demographics']['users']['mendeley']['by_status']:
                            users_other=data['demographics']['users']['mendeley']['by_status']['Other']
                            count+=1
                        else:
                            users_other=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Professor > Associate Professor' in data['demographics']['users']['mendeley']['by_status']:
                            users_prof_assoc=data['demographics']['users']['mendeley']['by_status']['Professor > Associate Professor']
                            count+=1
                        else:
                            users_prof_assoc=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Professor' in data['demographics']['users']['mendeley']['by_status']:
                            users_prof=data['demographics']['users']['mendeley']['by_status']['Professor']
                            count+=1
                        else:
                            users_prof=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Medicine and Dentistry' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_medi=data['demographics']['users']['mendeley']['by_discipline']['Medicine and Dentistry']
                            count+=1
                        else:
                            users_medi=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Social Sciences' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_ss=data['demographics']['users']['mendeley']['by_discipline']['Social Sciences']
                            count+=1
                        else:
                            users_ss=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Psychology' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_psych=data['demographics']['users']['mendeley']['by_discipline']['Psychology']
                            count+=1
                        else:
                            users_psych=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Earth and Planetary Sciences' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_earth=data['demographics']['users']['mendeley']['by_discipline']['Earth and Planetary Sciences']
                            count+=1
                        else:
                            users_earth=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Agricultural and Biological Sciences' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_agri=data['demographics']['users']['mendeley']['by_discipline']['Agricultural and Biological Sciences']
                            count+=1
                        else:
                            users_agri=0
                        if 'users' in data['demographics'] and 'mendeley' in data['demographics']['users'] and 'Arts and Humanities' in data['demographics']['users']['mendeley']['by_discipline']:
                            users_arts=data['demographics']['users']['mendeley']['by_discipline']['Arts and Humanities']
                            count+=1
                        else:
                            users_arts=0
                        if 'geo' in data['demographics'] and 'mendeley' in data['demographics']['geo']:
                            if 'US' in data['demographics']['geo']['mendeley']:
                                users_us=data['demographics']['geo']['mendeley']['US']
                                count+=1
                            else:
                                users_us=0
                            if 'TH' in data['demographics']['geo']['mendeley']:
                                users_th=data['demographics']['geo']['mendeley']['TH']
                                count+=1
                            else:
                                users_th=0
                            if 'IE' in data['demographics']['geo']['mendeley']:
                                users_ie=data['demographics']['geo']['mendeley']['IE']
                                count+=1
                            else:
                                users_ie=0
                            if 'ID' in data['demographics']['geo']['mendeley']:
                                users_id=data['demographics']['geo']['mendeley']['ID']
                                count+=1
                            else:
                                users_id=0
                            if 'AU' in data['demographics']['geo']['mendeley']:
                                users_au=data['demographics']['geo']['mendeley']['AU']
                                count+=1
                            else:
                                users_au=0
                            if 'GB' in data['demographics']['geo']['mendeley']:
                                users_gb=data['demographics']['geo']['mendeley']['GB']
                                count+=1
                            else:
                                users_gb=0
                        else:
                            users_us=0
                            users_th=0
                            users_ie=0
                            users_id=0
                            users_au=0
                            users_gb=0
                        if count>30:
                            datawriter.writerow([altmetric_id,mendeley_readers,citeulikereaders,connoteareaders,blog_users,blogs_posts_count,news_unique_users,total_posts_count,wiki_posts_count,facebook_users,facebook_posts,twitter_users,twitter_posts,citation_page,other_articles,mean,rank,perc,scored_higher_than,sample_size,users_lecturer,users_student_bachelor,users_student_master,users_student_pg,users_student_phd,users_student_doct,users_researcher,users_other,users_prof_assoc,users_prof,users_medi,users_ss,users_psych,users_earth,users_agri,users_arts,users_us,users_th,users_ie,users_id,users_au,users_gb,altmetric_score,altmetric_score_1y,altmetric_score_6m,altmetric_score_3m,altmetric_score_1m,altmetric_score_1w,altmetric_score_6d,altmetric_score_5d,altmetric_score_4d,altmetric_score_3d,altmetric_score_3d,altmetric_score_1d])
                            print(file_path)
