{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "4fd9f5eb",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'streamlit.runtime' has no attribute 'is_streamlit_running'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_1472\\4124072778.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mplotly\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexpress\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpx\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mruntime\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mif\u001b[0m \u001b[0mruntime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_streamlit_running\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m     \u001b[0mmain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'streamlit.runtime' has no attribute 'is_streamlit_running'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "from streamlit import runtime\n",
    "if runtime.is_streamlit_running():\n",
    "    main()\n",
    "else:\n",
    "    stcli.main()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "fc598cc7",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'streamlit' has no attribute '_is_running_with_streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_1472\\2350599837.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m st.set_page_config(page_title='PENDATAAN',\n\u001b[0m\u001b[0;32m      2\u001b[0m                   \u001b[0mpage_icon\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m':bar_chart:'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m                   \u001b[0mlayout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'wide'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m                   )\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\commands\\page_config.py\u001b[0m in \u001b[0;36mset_page_config\u001b[1;34m(page_title, page_icon, layout, initial_sidebar_state, menu_items)\u001b[0m\n\u001b[0;32m    158\u001b[0m         \u001b[0mset_menu_items_proto\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlowercase_menu_items\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmenu_items_proto\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    159\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 160\u001b[1;33m     \u001b[0mctx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mget_script_run_ctx\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    161\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mctx\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    162\u001b[0m         \u001b[1;32mreturn\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\scriptrunner\\script_run_context.py\u001b[0m in \u001b[0;36mget_script_run_ctx\u001b[1;34m()\u001b[0m\n\u001b[0;32m    143\u001b[0m         \u001b[0mthread\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mSCRIPT_RUN_CONTEXT_ATTR_NAME\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    144\u001b[0m     )\n\u001b[1;32m--> 145\u001b[1;33m     \u001b[1;32mif\u001b[0m \u001b[0mctx\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_is_running_with_streamlit\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    146\u001b[0m         \u001b[1;31m# Only warn about a missing ScriptRunContext if we were started\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    147\u001b[0m         \u001b[1;31m# via `streamlit run`. Otherwise, the user is likely running a\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'streamlit' has no attribute '_is_running_with_streamlit'"
     ]
    }
   ],
   "source": [
    "st.set_page_config(page_title='PENDATAAN',\n",
    "                  page_icon=':bar_chart:',\n",
    "                  layout='wide'\n",
    "                  )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "36b305a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_excel(\n",
    "    io = 'D:/Lewa67-UPDATE/Projek 2023/1. PETANI 2023/WIL 1/LAPANGAN/PROGRES PENDATAAN.xlsx',\n",
    "    engine = 'openpyxl',\n",
    "    sheet_name = 'Sheet1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee9ad092",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
