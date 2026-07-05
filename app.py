
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Inventory Management Dashboard", layout="wide")

data = pd.DataFrame({
    "Product":["Laptop","Mouse","Keyboard","Monitor","Printer","Router","SSD","Webcam","Chair","Desk"],
    "Category":["Electronics","Accessories","Accessories","Electronics","Office","Networking","Storage","Accessories","Furniture","Furniture"],
    "Supplier":["TechCorp","GearHub","GearHub","DisplayPro","OfficePlus","NetWorld","StorageX","VisionTech","FurniCo","FurniCo"],
    "Stock":[25,120,15,8,12,30,18,5,20,10],
    "Reorder":[10,40,20,10,10,15,15,10,8,5],
    "Price":[55000,600,1200,14000,9000,2500,4500,1800,7000,12000]
})
data["Value"]=data["Stock"]*data["Price"]

st.title("📦 Inventory Management Dashboard")

c1,c2,c3=st.columns(3)
c1.metric("Total Items",len(data))
c2.metric("Inventory Value",f"₹{data['Value'].sum():,}")
low=(data["Stock"]<data["Reorder"]).sum()
c3.metric("Low Stock Alerts",low)

st.subheader("⚠️ Low Stock")
st.dataframe(data[data["Stock"]<data["Reorder"]])

col1,col2=st.columns(2)
with col1:
    fig=px.bar(data,x="Category",y="Stock",color="Category",title="Stock by Category")
    st.plotly_chart(fig,use_container_width=True)
with col2:
    sup=data.groupby("Supplier",as_index=False)["Value"].sum()
    fig2=px.pie(sup,names="Supplier",values="Value",title="Supplier Analysis")
    st.plotly_chart(fig2,use_container_width=True)

st.subheader("Inventory Valuation")
fig3=px.bar(data.sort_values("Value",ascending=False),x="Product",y="Value",color="Category",title="Inventory Value by Product")
st.plotly_chart(fig3,use_container_width=True)

st.subheader("Inventory Data")
st.dataframe(data,use_container_width=True)
