#pragma once

#include "engine/alice/alice_codelet.hpp"
#include "messages/my_proto.hpp"

namespace isaac {
    class Sender : public alice::Codelet {
        public:
            void start() override;
            void tick() override;
            ISAAC_PARAM(int, number, 100);

            ISAAC_PROTO_TX(MyCustomProto, number);
    };
}

ISAAC_ALICE_REGISTER_CODELET(isaac::Sender);
