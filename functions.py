def ciao_ciao(x):
    return x**2


def time_intervals(intervals):
    posts_datatable = dt.fread("instagram_posts.csv")
    posts=posts_datatable.to_pandas()
    
    posts2=posts[['cts','post_id']]
    posts2['cts'] = pd.to_datetime(posts2['cts']).dt.time
    f, ax = plt.subplots(figsize=(15,5)) # set the size that you'd like (width, height)
    ax.ticklabel_format(useOffset=False, style='plain')
    cases=[]
    for time in intervals:
        initial = datetime.datetime.strptime(time[0][0], "%H:%M:%S").time()
        final = datetime.datetime.strptime(time[1][0], "%H:%M:%S").time()

        num=len(posts2[(posts2.cts < final) & (posts2.cts > initial)])
        
        interval=str(time[0][0])+'-'+str(time[1][0])

        plt.bar(interval, height= num)

        cases.append('{:,}'.format(num))
    ax.legend(cases)
    plt.show()


def searchpost(profile_id):
    df=posts[posts.profile_id == profile_id]
    return df[['post_id','profile_id','numbr_likes','number_comments','location_id','post_type']]


    
def top_posts(n):
    df=pd.DataFrame(columns=['profile_id','post_id'])
    top=profiles.sort_values(by='n_posts', ascending=False).head(n)
    for profile_id in top.profile_id.values:
        df=pd.concat([df,searchpost(profile_id)])
    return df