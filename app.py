import streamlit as st
from PIL import Image
from label_text import ntu120, nucla

def vis_part_tsne(db='NTU-120', part='Global', label=0):
    if db=='NTU-120':
        if label==-1: label=120
        im_path=f'tsne/{part.lower()}/ntu_tsne/cluster_ntu_{label}.png'
    if db=='NUCLA':
        if label==-1: label=10
        im_path=f'tsne/{part.lower()}/nucla_tsne/cluster_nucla_{label}.png'
    image=Image.open(im_path)
    
    if label == 120 or label == 10: st.image(image,width=1500)
    else: st.image(image, use_container_width=True)
    
    
def vis_part_graph(db='NTU-120', part='Global', label=0):
    if label == -1: return
    if db=='NTU-120':
        im_path=f'tsne/{part.lower()}/ntu_tsne/graph_ntu_{label}.png'
    if db=='NUCLA':
        im_path=f'tsne/{part.lower()}/nucla_tsne/graph_nucla_{label}.png'
    image=Image.open(im_path)
    
    st.image(image, use_container_width=True)   
    
    
if __name__ == '__main__':
 
    st.set_page_config(layout="wide")
    st.sidebar.title("Skeleton Visualization")
    db_opt=['NTU-120', 'NUCLA']
    part_opt=['Global', 'Head', 'Hand', 'Hip', 'Foot']
    selected_db = st.sidebar.selectbox('Dataset:',db_opt)
    selected_part = st.sidebar.selectbox('Body-part:', part_opt)
    selected_ntu_label = st.sidebar.selectbox('NTU-120 Labels:', ['All']+ntu120)
    selected_nucla_label = st.sidebar.selectbox('NUCLA Labels:', ['All']+nucla)
    
    ntu_dict = {value: index for index, value in enumerate(ntu120)}
    nucla_dict = {value: index for index, value in enumerate(nucla)}

    if st.sidebar.button('Submit'):
        st.empty()
        if selected_db==db_opt[0]:
            st.markdown(f'### Action: {selected_ntu_label}')
            if selected_ntu_label == 'All': label_idx=-1
            else: label_idx=ntu_dict[selected_ntu_label]
            if label_idx != -1:
                col1, col2 = st.columns([2, 1])
                with col1: vis_part_tsne(db=selected_db,part=selected_part,label=label_idx)
                with col2:
                    video_file = open(f'joint_videos/label_{label_idx}.mp4','rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)
                    vis_part_graph(db=selected_db,part=selected_part,label=label_idx)
            else: vis_part_tsne(db=selected_db,part=selected_part,label=label_idx)
        if selected_db==db_opt[1]:
            st.markdown(f'### Action: {selected_nucla_label}')
            if selected_nucla_label == 'All': label_idx=-1
            else: label_idx=nucla_dict[selected_nucla_label]
            if label_idx != -1:
                col1, col2 = st.columns([2, 1])
                with col1: vis_part_tsne(db=selected_db,part=selected_part,label=label_idx)
                with col2:
                    video_file = open(f'nucla_videos/ucla_{label_idx}.mp4','rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)
                    vis_part_graph(db=selected_db,part=selected_part,label=label_idx)
                
            else: vis_part_tsne(db=selected_db,part=selected_part,label=label_idx)
              
    #st.sidebar.markdown("Skeleton encoder: \n HD-GCN(ICCV''23)+GAP(ICCV''23)")  
        
  