import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

data_df = pd.read_csv("cleaned_day.csv")

with st.sidebar:
    st.image("https://th.bing.com/th/id/OIP.Od6oeCUSyvgBkkVGNOE7DwHaE8?w=266&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7")
    st.markdown(
        """
        # Bike Rentals
        let's live healthy together, pollution-free clean environment

        """
    )
st.header('Bicycle Rental Analysis')

st.subheader("Trends in the number of cyclists in recent years", divider="gray")

data_df['mnth'] = pd.Categorical(data_df['mnth'], categories=
    ['January','February','March','April','May','June','July','August','September','October','November','December'],
    ordered=True)

monthly_counts = data_df.groupby(by=["mnth","yr"]).agg({
    "cnt": "sum"
}).reset_index()

monthly_counts = monthly_counts.sort_values(by=['yr', 'mnth'])

monthly_counts['mnth_short'] = monthly_counts['mnth'].str[:3]

palette = ["black", "red"]

sns.lineplot(
    data=monthly_counts,
    x="mnth_short",
    y="cnt",
    hue="yr",
    palette=palette,
    marker="o")

plt.title("Trend bike Rent")
plt.xlabel(None)
plt.ylabel(None)
plt.legend(title="Tahun", loc="upper right")
plt.tight_layout()

st.pyplot(plt)


st.subheader('The effect of seasonality on the number of bike rentals')

seasonal_analysis = data_df.groupby('season').agg({'cnt': ['max', 'min', 'mean']})

seasonal_analysis.plot(kind='bar', figsize=(10, 6))
plt.title('Seasonal Analysis of number of bike rentals')
plt.xlabel('Season')
plt.ylabel(None)
plt.legend(['Max', 'Min', 'Mean'])

st.pyplot(plt)


st.subheader('Days when there are more and less bike rentals')
weekday_analysis = data_df.groupby(by='weekday').agg({
    'cnt':['max','min','mean']
}).reindex(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

weekday_analysis.plot(kind='line', figsize=(10, 6))
plt.title('Weekday Analysis of number of bike rentals')
plt.xlabel(None)
plt.ylabel(None)
plt.legend(['Max', 'Min', 'Mean'])
st.pyplot(plt)

st.caption('Copyright (c) 2024')