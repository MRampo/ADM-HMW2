import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def time_intervals(posts,intervals,variable,mean=False):

    posts2=posts[['cts',variable]]
    posts2['cts'] = pd.to_datetime(posts2['cts']).dt.time

    f, ax = plt.subplots(figsize=(15,5)) # set the size that you'd like (width, height)
    ax.ticklabel_format(useOffset=False, style='plain')
    
    cases=[]
    if mean == False:
        for time in intervals:
            initial = datetime.datetime.strptime(time[0][0], "%H:%M:%S").time()
            final = datetime.datetime.strptime(time[1][0], "%H:%M:%S").time()

            num=len(posts2[(posts2.cts < final) & (posts2.cts > initial)])
        
            interval=str(time[0][0])+'-'+str(time[1][0])

            plt.bar(interval, height= num)

            cases.append('{:,}'.format(num))
    else:
         for time in intervals:
            initial = datetime.datetime.strptime(time[0][0], "%H:%M:%S").time()
            final = datetime.datetime.strptime(time[1][0], "%H:%M:%S").time()

            num=posts2[(posts2.cts < final) & (posts2.cts > initial)].sum()/len(posts2[(posts2.cts < final) & (posts2.cts > initial)])
        
            interval=str(time[0][0])+'-'+str(time[1][0])

            plt.bar(interval, height= num)

            cases.append('{:,}'.format(int(np.round(num,0))))

    ax.legend(cases)
    plt.show()


def searchpost(posts,profile_id):
    df=posts[posts.profile_id == profile_id]
    return df[['post_id','profile_id','numbr_likes','number_comments','location_id','post_type','cts']]

def top_posts(profiles,posts,n):

    df=pd.DataFrame(columns=['profile_id','post_id'])
    top=profiles.sort_values(by='n_posts', ascending=False).head(n)
    for profile_id in top.profile_id.values:
        df=pd.concat([df,searchpost(posts,profile_id)])
    return df