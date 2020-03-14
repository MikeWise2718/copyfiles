import os
import shutil
import argparse
import lgger as lgg

parser = argparse.ArgumentParser(description='copyfile --sdir sourecdir --dir destdir')
parser.add_argument('--sdir', type=str, default=".",   help='source directory',required=False)
parser.add_argument('--ddir', type=str, default="dest", help='dest directory',required=False)

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


def copyFromTo(sdir,ddir):
    for (fdname,fname) in listfiles:
        sfname = f"{sdir}/{fdname}{fname}"
        dfname = f"{ddir}/{fdname}{fname}"
        dddir = f"{ddir}/{fdname}"
        fclr = lgg.cC
        if not os.path.exists(dddir):
            lgg.info(f"Creating directory {dddir}",lgg.cR)
            os.makedirs(dddir)
        elif os.path.exists(dfname):
            fclr = lgg.cB
        lgg.info(f"copy from {sfname} to {dfname}",fclr)
        shutil.copyfile(sfname,dfname)

sdir = args.sdir
ddir = args.ddir

lgg.info(f"Copying {len(listfiles)} files from {sdir} to {ddir}",lgg.cY)

copyFromTo(args.sdir,args.ddir)