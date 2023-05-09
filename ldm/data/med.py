dataset_records = {"dataset_test":{"gastro_cancer/xiehe_far_1":[1],},
                "dataset1":
                {"gastro_cancer/xiehe_far_1":[1], #0
                "gastro_cancer/xiehe_far_2":[1], #1
                "gastro_cancer/xiangya_far_2021":[1], #2
                "gastro_cancer/xiangya_far_2022":[1], #3
                },
                "dataset2":
                {"gastro_cancer/xiehe_far_1":[1], #0
                "gastro_cancer/xiehe_far_2":[1], #1
                "gastro_cancer/xiangya_far_2021":[1], #2
                "gastro_cancer/xiangya_far_2022":[1], #3
                "gastro_cancer/gastro8-12/2021-2022年癌变已标注/20221111/2021_2022_癌变_20221111":[1,4,5], #4
                "gastro_cancer/gastro8-12/低级别_2021_2022已标注/2021_2022_低级别_20221110":[1,4,5], #5
                "gastro_cancer/gastro8-12/协和2022_第一批胃早癌视频裁图已标注/20221115/癌变2022_20221115":[1,4,5], #6
                "gastro_cancer/gastro8-12/协和2022_第二批胃早癌视频裁图已标注/协和_2022_癌变_2_20221117":[1,4,5], #7
                "gastro_cancer/gastro8-12/协和21-11月~2022-5癌变已标注/协和2021-11月_2022-5癌变_20221121":[1,4,5], #8
                },}

def check_and_fix_bbox(bbox,width,height):
    bbox[0] = 1 if bbox[0]<0 else bbox[0]
    bbox[1] = 1 if bbox[1]<0 else bbox[1]
    bbox[2] = width-bbox[0] if bbox[0]+bbox[2]>width else bbox[2]
    bbox[3] = height-bbox[1] if bbox[1]+bbox[3]>height else bbox[3]    
    return [int(value) for value in bbox] 