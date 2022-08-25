import pandas as pd
import tensorflow as tf
import streamlit as st
from sklearn.preprocessing import StandardScaler


model = tf.keras.models.load_model('model.h5')
market_segment = ["Complementary", "Groups", "Travel Agent/Operator", "Corporate"]
col1, col2, col3, col4 = st.columns(4)

with col1:
    Age = int(st.number_input("Customer Age"))
with col2:
    RoomNights = int(st.number_input("Enter Rooms/nights"))
with col3:
    PersonsNights = int(st.number_input("Enter persons/nights"))
with col4:
    BookingsCanceled = st.selectbox("Bookings canceled ?", ["yes", "No"])
    if BookingsCanceled == "yes":
        BookingsCanceled = 1
    else:
        BookingsCanceled = 0


col5, col6, col7, col8 = st.columns(4)

with col5:
    LodgingRevenue = int(st.number_input("Revenue"))
with col6:
    OtherRevenue = int(st.number_input("Other Revenue"))
with col7:
    BookingsNoShowed = int(st.number_input("No bookings showed"))
with col8:
    AverageLeadTime = int(st.number_input("lead_time(Avg) booking"))

col9, col10, col11, col12 = st.columns(4)

with col9:
    DistributionChannel_Electronic_Distribution = st.selectbox("Distribution channel electronic ", ["yes", "No"])
    if DistributionChannel_Electronic_Distribution == "yes":
        DistributionChannel_Electronic_Distribution = 1
    else:
        DistributionChannel_Electronic_Distribution = 0

with col10:
    market = st.selectbox("Select market segment", market_segment)
    if market == "Complementary":
        MarketSegment_Complementary = 1
    else:
        MarketSegment_Complementary = 0
    if market == "Groups":
        MarketSegment_Groups = 1
    else:
        MarketSegment_Groups = 0
    if market == "Travel Agent/Operator":
        MarketSegment_Travel_Agent_Operator = 1
    else:
        MarketSegment_Travel_Agent_Operator = 0
    if market == "Corporate":
        MarketSegment_Corporate = 1
    else:
        MarketSegment_Corporate = 0

with col11:
    DaysSinceFirstStay = int(st.number_input("Number of days he first stay"))
with col12:
    DaysSinceLastStay = int(st.number_input("Number of days he last stay"))
st.write("Select 1 where customer chosen below parameter otherwise select 0")
col13, col14, col15, col16, col17 = st.columns(5)
with col13:
    SRMediumFloor = int(st.selectbox("Medium floor", [0, 1]))
with col14:
    SRKingSizeBed = int(st.selectbox("king size bed", [0, 1]))
with col15:
    SRAwayFromElevator = int(st.selectbox("Away from elevator", [0, 1]))
with col16:
    SRNearElevator = int(st.selectbox("Near from elevator", [0, 1]))
with col17:
    SRAccessibleRoom = int(st.selectbox("Accessible Room", [0, 1]))

if st.button("Submit"):
    input = {"x1":[RoomNights], "x2":[PersonsNights], "x3":[BookingsCanceled], "x4":[DaysSinceFirstStay], "x5":[LodgingRevenue], "x6":[DaysSinceLastStay],
             "x7":[OtherRevenue], "x8":[BookingsNoShowed], "x9":[AverageLeadTime], "x10":[MarketSegment_Corporate], "x11":[Age], "x12":[MarketSegment_Complementary],
             "x13":[DistributionChannel_Electronic_Distribution], "x14":[MarketSegment_Groups], "x15":[SRMediumFloor], "x16":[SRKingSizeBed], "x17":[MarketSegment_Travel_Agent_Operator],
             "x18":[SRAwayFromElevator], "x19":[SRAccessibleRoom], "x20":[SRAwayFromElevator]}
    sc = StandardScaler()
    df = pd.DataFrame(input)
    scaled_input = sc.fit_transform(df)
    prediction = model.predict(scaled_input)
    st.header(f"Cutomer checked IN {prediction[0][0]}" )
