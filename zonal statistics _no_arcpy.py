import os,numpy,pandas,xarray,rioxarray,rasterio
sh=xarray.open_rasterio(r"K:\RA\shahrestan_.tif")
place=r"K:\RA\mean_daily_tmax\mean_daily_tmax"
pandas.DataFrame(columns=["sh","value","valdate"]).to_csv(r"G:\excel1\New Text Document.txt")
for file in numpy.sort([item for item in os.listdir(place) if item.endswith(".tif")]):
    data=xarray.open_rasterio(os.path.join(place,file))
    frame=pandas.DataFrame(numpy.array([sh.values.ravel(),data.values.ravel()]).T,columns=["sh","value"]).dropna()
    frame=frame[(~(frame['value']>=60.))&(~(frame['value']<=-60.))]
    frame=frame.groupby("sh").mean()
    frame["valdate"]=file.replace(".txt","")
    frame.to_csv(r"G:\excel1\New Text Document.txt",header=False,mode='a')
    print(file)