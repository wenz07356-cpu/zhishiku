import copy
import json
import uuid
from typing import TypedDict
from app.shared.runtime.logger import logger
class ImportGraphState(TypedDict):
    #任务追踪
    task_id:str
    #传入文件地址
    local_file_path:str
    #判断结果
    is_md_read_enabled:bool
    is_pdf_read_enabled:bool
    #兜底item_name
    file_title:str
    #pdf解析入口文件地址
    pdf_path:str
    # pdf转出md文件地址
    local_dir:str
    #md文件/图片地址
    md_path: str
    #切片原材料
    md_content:str
    #载体
    chunks:list
    #文档主语
    item_name:str
    #向量数据库
    embedding_content:list

graph_default_state: ImportGraphState = {
    'task_id': None,
    'local_file_path': None,
    'is_md_read_enabled': False,
    'is_pdf_read_enabled': False,
    'file_title': None,
    'pdf_path': None,
    'local_dir': None,
    'md_path': None,
    'md_content': None,
    'chunks': None,
    'item_name': None,
    'embedding_content': [],
}

def create_default_state(**overrides) -> ImportGraphState:
    new_state = copy.deepcopy(graph_default_state)
    new_state.update(overrides)
    return new_state

def get_default_state() -> ImportGraphState:
    return copy.deepcopy(graph_default_state)

if __name__ == '__main__':
    state = create_default_state(task_id="uuid.uuid4()",local_file_path = "**")
    logger.info(json.dumps(state, indent=2,ensure_ascii=False))

