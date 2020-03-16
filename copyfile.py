import os
import shutil
import argparse
import lgger as lgg
import timeit

parser = argparse.ArgumentParser(description='copyfile --sdir sourecdir --dir destdir')
parser.add_argument('--sdir', type=str, default=".",   help='source directory',required=False)
parser.add_argument('--ddir', type=str, default="dest", help='dest directory',required=False)
parser.add_argument('--exec', type=bool, default=True, help='dest directory',required=False)

args = parser.parse_args()

listfiles=[
    ["com.unity.ml-agents/Runtime/","Academy.cs"],
    ["com.unity.ml-agents/Runtime/","Agent.cs"],
    ["com.unity.ml-agents/Runtime/Communiticator/","RpcCommunicator.cs"],
    ["ml-agents/ml-agents/mlagents/trainers/","agent_processor.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","base_env.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","communicator.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","environment.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","exception.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","rpc_communicator.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","rpc_utils.py"],
    ["ml-agents/protobf-deffinitions/proto/mlagents_envs/communicator_objects/","environment_statistics.proto"],
    ["ml-agents/protobf-deffinitions/proto/mlagents_envs/communicator_objects/","unity_rl_output.proto"],
    ["Project/Assets/ML-Agents/Examples/FoodCollector/Scripts/","FoodCollectorAgent.cs"],
    ["Project/Assets/ML-Agents/Examples/FoodCollector/Scripts/","FoodCollectorSettings.cs"]
    ]


def copyFromTo(sdir,ddir,execute):
    overwrittenfiles = 0
    overwrittenbytes = 0
    for (fdname,fname) in listfiles:
        sfname = f"{sdir}/{fdname}{fname}"
        dfname = f"{ddir}/{fdname}{fname}"
        dddir = f"{ddir}/{fdname}"
        fclr = lgg.cC 
        ovbytes = 0
        if execute and (not os.path.exists(dddir)):
            lgg.info(f"Creating directory {dddir}",lgg.cR)
            os.makedirs(dddir)
        if os.path.exists(dfname):
            fclr = lgg.cG
            ftats = os.stat(dfname)
            ovbytes = ftats.st_size
            overwrittenbytes += ovbytes
            overwrittenfiles += 1
        execword = "execute" if execute else "fake"
        lgg.info(f"{execword} copy from {sfname} to {dfname} overwrittenbytes:{ovbytes}",fclr)
        if execute:
            shutil.copyfile(sfname,dfname)
    return (overwrittenfiles,overwrittenbytes)

sdir = args.sdir
ddir = args.ddir
execute = args.exec

lgg.info(f"Copying {len(listfiles)} files from {sdir} to {ddir} execute:{execute}",lgg.cY)

start = timeit.timeit()
(ovfiles,ovbytes) = copyFromTo(sdir,ddir,execute)
elap = timeit.timeit()-start 

exword = "" if execute else "Would have "
lgg.info(f"{exword} Overwritten files:{ovfiles}  overwritenbytes:{ovbytes} secs:{round(elap,3)} ",lgg.cY)
